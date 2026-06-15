import sys
import io
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

try:
    from art import text2art
except ImportError:
    def text2art(text):
        return text


class LotteryModel(nn.Module):
    def __init__(self, num_features, max_value, window_size=10, hidden_size=256, dropout=0.2):
        super().__init__()
        self.num_features = num_features
        self.window_size = window_size
        self.num_classes = max_value + 1

        input_dim = window_size * (max_value + 1)
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_size),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, hidden_size),
            nn.BatchNorm1d(hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, num_features * (max_value + 1)),
        )

    def forward(self, x):
        batch = x.size(0)
        one_hot = torch.nn.functional.one_hot(x, num_classes=self.num_classes)
        one_hot = one_hot.view(batch, self.window_size, self.num_features, self.num_classes)
        multi_hot = torch.clamp(one_hot.sum(dim=2), 0, 1)
        x_flat = multi_hot.reshape(batch, self.window_size * self.num_classes).float()
        out = self.net(x_flat)
        return out.view(batch, self.num_features, self.num_classes)


def print_intro():
    try:
        ascii_art = text2art("AiLotto")
        print("=" * 60)
        print(ascii_art)
        print("Lottery prediction artificial intelligence (PyTorch)")
        print("=" * 60)
    except:
        pass


def load_data():
    try:
        import os
        if not os.path.exists('data.txt'):
            raise FileNotFoundError("Error: 'data.txt' not found in the current directory.")

        with open('data.txt', 'r', encoding='utf-8') as f:
            raw = f.read().replace('\ufeff', '')
        data = np.genfromtxt(io.StringIO(raw), delimiter=',', dtype=int)

        if data.size == 0:
            raise ValueError("Error: 'data.txt' is empty or contains improperly formatted data.")
        data[data == -1] = 0

        max_value = int(np.max(data))
        return data, max_value
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error loading data: {str(e)}")
        sys.exit(1)


def create_sequences(data, window_size=10):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size].flatten())
        y.append(data[i+window_size])
    X = np.array(X)
    y = np.array(y)
    split = int(0.8 * len(X))
    return X[:split], y[:split], X[split:], y[split:]


def create_data_loaders(X_train, y_train, X_val, y_val, batch_size=32):
    train_dataset = TensorDataset(
        torch.tensor(X_train, dtype=torch.long),
        torch.tensor(y_train, dtype=torch.long)
    )
    val_dataset = TensorDataset(
        torch.tensor(X_val, dtype=torch.long),
        torch.tensor(y_val, dtype=torch.long)
    )
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    return train_loader, val_loader


def train_model(model, train_loader, val_loader, num_classes, num_epochs=300, lr=0.001,
                weight_decay=5e-5, patience=25, device='cpu'):
    model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='max', factor=0.5, patience=10, min_lr=1e-6
    )

    best_val_acc = 0.0
    best_state = None
    patience_counter = 0

    print("Starting model training...")
    for epoch in range(num_epochs):
        model.train()
        train_loss = 0.0
        train_correct = 0
        train_total = 0

        for inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            outputs = outputs.view(-1, num_classes)
            targets_flat = targets.view(-1)
            loss = criterion(outputs, targets_flat)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            train_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            train_total += targets_flat.size(0)
            train_correct += (predicted == targets_flat).sum().item()

        model.eval()
        val_loss = 0.0
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for inputs, targets in val_loader:
                inputs, targets = inputs.to(device), targets.to(device)
                outputs = model(inputs)
                outputs = outputs.view(-1, num_classes)
                targets_flat = targets.view(-1)
                loss = criterion(outputs, targets_flat)
                val_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                val_total += targets_flat.size(0)
                val_correct += (predicted == targets_flat).sum().item()

        train_acc = 100.0 * train_correct / train_total
        val_acc = 100.0 * val_correct / val_total

        scheduler.step(val_acc)

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = model.state_dict()
            patience_counter = 0
        else:
            patience_counter += 1

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}] "
                  f"Train Loss: {train_loss/len(train_loader):.4f} "
                  f"Train Acc: {train_acc:.2f}% "
                  f"Val Acc: {val_acc:.2f}%")

#       if patience_counter >= patience:
#           print(f"Early stopping at epoch {epoch+1}")
#           break

    model.load_state_dict(best_state)
    print(f"Best validation accuracy: {best_val_acc:.2f}%")
    return model


def predict_numbers(model, input_data, num_features, device='cpu'):
    model.eval()
    model.to(device)
    input_tensor = torch.tensor(input_data, dtype=torch.long)
    if input_tensor.dim() == 1:
        input_tensor = input_tensor.unsqueeze(0)
    input_tensor = input_tensor.to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=-1)
        _, predicted = torch.topk(probs, k=1, dim=-1)
        predicted = predicted.squeeze(-1)

    return predicted.cpu().numpy()


def print_predicted_numbers(predicted_numbers):
    try:
        print("-" * 60)
        print("Predicted Numbers:")
        if predicted_numbers.size > 0:
            print(', '.join(map(str, predicted_numbers[0])))
        else:
            print("No predictions were generated.")
        print("=" * 60)
        print("Disclaimer: Lottery prediction is inherently speculative. Use for entertainment purposes only.")
        print("=" * 60)
    except Exception as e:
        print(f"Error printing predictions: {str(e)}")
        sys.exit(1)


def main():
    try:
        print_intro()

        print("Loading and preparing data...")
        all_data, max_value = load_data()
        print(f"Max lottery number: {max_value}")
        print(f"Total draws: {all_data.shape[0]}")

        if all_data.ndim < 2:
            raise ValueError("Data must have at least 2 dimensions.")
        num_features = all_data.shape[1]
        print(f"Numbers per draw: {num_features}")

        window_size = 10
        print(f"Window size: {window_size} (past draws used to predict next)")

        print("Creating sliding window sequences...")
        X_train, y_train, X_val, y_val = create_sequences(all_data, window_size)
        print(f"Training sequences: {len(X_train)}, Validation sequences: {len(X_val)}")

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")

        print("Creating model...")
        model = LotteryModel(num_features, max_value, window_size)
        print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")

        train_loader, val_loader = create_data_loaders(X_train, y_train, X_val, y_val)
        train_model(model, train_loader, val_loader, max_value + 1, device=device)

        prediction_input = X_val[-1:]
        predicted_numbers = predict_numbers(model, prediction_input, num_features, device=device)

        print_predicted_numbers(predicted_numbers)
        print("AiLotto finished.")

    except FileNotFoundError as e:
        print(f"Fatal Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Fatal Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
