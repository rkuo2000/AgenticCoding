import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Configuration
WIDTH, HEIGHT = 400, 400
DOT_COLOR = (118, 185, 0)  # NVIDIA Green
BG_COLOR = (0, 0, 0)
NUM_POINTS = 2000
FPS = 20
MORPH_DURATION = 1.5  # seconds
SCATTER_DURATION = 0.5  # seconds

def get_taipei_101_points(n):
    points = []
    # Simplified Taipei 101: 8 segments
    segments = 8
    seg_height = 30
    base_width = 60
    for i in range(segments):
        w = base_width * (1 - i/segments * 0.6)
        h_start = HEIGHT - 50 - i * seg_height
        # Rectangular segment
        # Top and bottom edges
        for x in np.linspace(-w/2, w/2, int(w)):
            points.append((x + WIDTH/2, h_start))
            points.append((x + WIDTH/2, h_start - seg_height))
        # Side edges
        for y in np.linspace(h_start - seg_height, h_start, int(seg_height)):
            points.append((-w/2 + WIDTH/2, y))
            points.append((w/2 + WIDTH/2, y))
    
    # Randomize if we have too few or too many
    while len(points) < n:
        points.append((np.random.uniform(0, WIDTH), np.random.uniform(0, HEIGHT)))
    return np.array(points[:n])

def get_text_points(text, n):
    # Create a temporary image to draw text and sample points
    img = Image.new('L', (WIDTH, HEIGHT), 0)
    draw = ImageDraw.Draw(img)
    # Attempt to use a default font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Center text
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((WIDTH/2 - tw/2, HEIGHT/2 - th/2), text, fill=255, font=font)
    
    # Sample pixels that are white
    pixels = np.argwhere(np.array(img) > 0)
    if len(pixels) == 0:
        return np.random.rand(n, 2) * [WIDTH, HEIGHT]
    
    # Resample to exactly n points
    indices = np.random.choice(len(pixels), n, replace=True)
    pts = pixels[indices]
    # Swap x and y because argwhere returns (row, col)
    return np.array([[p[1], p[0]] for p in pts])

def get_logo_points(n):
    # NVIDIA Eye: Outer ellipse and inner circle
    points = []
    # Outer eye (ellipse)
    t = np.linspace(0, 2*np.pi, int(n*0.7))
    x = 80 * np.cos(t) + WIDTH/2
    y = 40 * np.sin(t) + HEIGHT/2
    for px, py in zip(x, y):
        points.append((px, py))
    
    # Inner eye (circle/pupil)
    t2 = np.linspace(0, 2*np.pi, int(n*0.3))
    x2 = 20 * np.cos(t2) + WIDTH/2
    y2 = 20 * np.sin(t2) + HEIGHT/2
    for px, py in zip(x2, y2):
        points.append((px, py))
        
    return np.array(points[:n])

def get_scatter_points(n):
    return np.random.rand(n, 2) * [WIDTH, HEIGHT]

def interpolate(start, end, alpha):
    return start + (end - start) * alpha

def render_frame(points):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    for p in points:
        draw.ellipse([p[0]-1, p[1]-1, p[0]+1, p[1]+1], fill=DOT_COLOR)
    return img

def main():
    # Define target states
    s_scatter = get_scatter_points(NUM_POINTS)
    s_taipei = get_taipei_101_points(NUM_POINTS)
    s_text = get_text_points("GTC TAIPEI 2026", NUM_POINTS)
    s_logo = get_logo_points(NUM_POINTS)
    
    frames = []
    
    # Sequence of points sets and durations
    # (start, end, duration_secs)
    sequence = [
        (s_scatter, s_taipei, MORPH_DURATION),
        (s_taipei, s_text, MORPH_DURATION),
        (s_text, s_logo, MORPH_DURATION),
        (s_logo, s_scatter, SCATTER_DURATION),
    ]
    
    for start, end, duration in sequence:
        num_frames = int(duration * FPS)
        for i in range(num_frames):
            alpha = i / num_frames
            points = interpolate(start, end, alpha)
            frames.append(render_frame(points))
            
    # Save as GIF
    frames[0].save('nvidia_gtc.gif', save_all=True, append_images=frames[1:], duration=1000//FPS, loop=0)
    print("GIF saved as nvidia_gtc.gif")

if __name__ == "__main__":
    main()
