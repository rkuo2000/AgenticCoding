import csv
import re
from datetime import datetime
from collections import defaultdict

# Read all CSV files
files = [
    'bankbook/bankbook-1150119.csv',
    'bankbook/bankbook-1150205.csv',
    'bankbook/bankbook-1150212.csv',
    'bankbook/bankbook-1150223.csv',
    'bankbook/bankbook-1150225.csv'
]

all_transactions = []

for f in files:
    with open(f, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date_str = row['年月日'].strip()
            if not date_str or not date_str[0].isdigit():
                continue
            # Convert 1150202 to 2026-02-02
            try:
                year = int(date_str[:3]) + 1911
                month = int(date_str[3:5])
                day = int(date_str[5:7])
                date_obj = datetime(year, month, day)
            except:
                continue
            
            summary = row['摘要'].strip()
            expense = int(row['支出']) if row['支出'].strip() else 0
            income = int(row['存入']) if row['存入'].strip() else 0
            balance = int(row['結存']) if row['結存'].strip() else 0
            note = row['備註'].strip()
            
            all_transactions.append({
                'date': date_obj,
                'date_str': date_str,
                'summary': summary,
                'expense': expense,
                'income': income,
                'balance': balance,
                'note': note
            })

# Sort by date
all_transactions.sort(key=lambda x: x['date'])

# Filter February 2026 (115/02)
feb_transactions = [t for t in all_transactions if t['date'].year == 2026 and t['date'].month == 2]

# Categorize income
general_income = []  # 管理費相關
other_income = []    # 其他收入

# Categorize expense
fixed_expense = []   # 固定支出
variable_expense = [] # 非固定支出

for t in feb_transactions:
    summary = t['summary']
    note = t['note']
    amount = t['income'] if t['income'] > 0 else t['expense']
    is_income = t['income'] > 0
    
    if is_income:
        # Check if it's 管理費 related
        if '管理' in summary or '管理' in note:
            general_income.append({'date': t['date_str'], 'summary': summary, 'note': note, 'amount': amount})
        else:
            other_income.append({'date': t['date_str'], 'summary': summary, 'note': note, 'amount': amount})
    else:
        # Expense categorization
        is_fixed = False
        fixed_keywords = ['保全', '清潔', '電梯', '機電', '網路', '水費', '電費', '台水', '台電', '中華電信']
        for kw in fixed_keywords:
            if kw in summary or kw in note:
                is_fixed = True
                break
        # Also check for fixed expense patterns in note
        if '1月' in note and ('保全' in note or '清潔' in note or '電梯' in note or '機電' in note or '網路' in note):
            is_fixed = True
        
        if is_fixed:
            fixed_expense.append({'date': t['date_str'], 'summary': summary, 'note': note, 'amount': amount})
        else:
            variable_expense.append({'date': t['date_str'], 'summary': summary, 'note': note, 'amount': amount})

# Calculate subtotals
general_income_total = sum(x['amount'] for x in general_income)
other_income_total = sum(x['amount'] for x in other_income)
income_total = general_income_total + other_income_total

fixed_expense_total = sum(x['amount'] for x in fixed_expense)
variable_expense_total = sum(x['amount'] for x in variable_expense)
expense_total = fixed_expense_total + variable_expense_total

# Previous period balance (last Jan transaction)
jan_transactions = [t for t in all_transactions if t['date'].year == 2026 and t['date'].month == 1]
prev_balance = jan_transactions[-1]['balance'] if jan_transactions else 0

# Current period balance (last Feb transaction)
current_balance = feb_transactions[-1]['balance'] if feb_transactions else 0

# Generate finance.md
md = """## 財務報表

---
### 收支表格

#### 收入項目
---
**一般收入**：
"""
for item in general_income:
    md += f"- {item['date']} {item['summary']} {item['note']}：{item['amount']:,}\n"
md += f"\n一般收入小計：{general_income_total:,}\n\n"

md += "**其他收入**：\n"
for item in other_income:
    md += f"- {item['date']} {item['summary']} {item['note']}：{item['amount']:,}\n"
md += f"\n其他收入小計：{other_income_total:,}\n\n"

md += f"**收入合計**：{income_total:,}\n\n"

md += """#### 支出項目
---
**固定支出**：
"""
for item in fixed_expense:
    md += f"- {item['date']} {item['summary']} {item['note']}：{item['amount']:,}\n"
md += f"\n固定支出小計：{fixed_expense_total:,}\n\n"

md += "**非固定支出**：\n"
for item in variable_expense:
    md += f"- {item['date']} {item['summary']} {item['note']}：{item['amount']:,}\n"
md += f"\n非固定支出小計：{variable_expense_total:,}\n\n"

md += f"**支出合計**：{expense_total:,}\n\n"

md += """---
### 財務總結
"""
md += f"- **上期結餘**：{prev_balance:,}\n"
md += f"- **本期收入**：{income_total:,}\n"
md += f"- **本期支出**：{expense_total:,}\n"
md += f"- **本期結餘**：{current_balance:,}\n"

with open('finance.md', 'w', encoding='utf-8') as f:
    f.write(md)

print("finance.md generated successfully!")
print(f"General Income: {general_income_total:,}")
print(f"Other Income: {other_income_total:,}")
print(f"Total Income: {income_total:,}")
print(f"Fixed Expense: {fixed_expense_total:,}")
print(f"Variable Expense: {variable_expense_total:,}")
print(f"Total Expense: {expense_total:,}")
print(f"Prev Balance: {prev_balance:,}")
print(f"Current Balance: {current_balance:,}")
