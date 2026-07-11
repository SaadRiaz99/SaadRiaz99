import math
import random

random.seed(42)

# Canvas
W = 1280
H = 640
SPACING = 5
MAX_R = 2.8
BG = "#000000"
FG = "#ffffff"

def g(x, y, cx, cy, sx, sy):
    return math.exp(-((x - cx) ** 2 / (2 * sx ** 2) + (y - cy) ** 2 / (2 * sy ** 2)))

def em(x, y, cx, cy, rx, ry):
    v = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
    return max(0, 1 - v) if v < 1 else 0

def ring(x, y, cx, cy, r_inner, r_outer, sharpness=4):
    d = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    if d < r_inner:
        return max(0, 1 - (r_inner - d) / max(r_inner, 1)) * 0.3
    elif d < r_outer:
        t = (d - r_inner) / (r_outer - r_inner)
        return max(0, (1 - t) ** sharpness)
    return 0

def compute(x, y):
    fade = max(0, 1 - (max(0, x / W) / 0.62) ** 2.2)
    if fade < 0.01:
        return 0

    v = 0

    # --- Head shape (main) ---
    v += em(x, y, 340, 320, 185, 230) * 0.55

    # --- Hair mass ---
    v += em(x, y, 335, 130, 195, 100) * 0.85
    v += em(x, y, 250, 110, 80, 60) * 0.7
    v += em(x, y, 420, 115, 80, 60) * 0.7
    v += g(x, y, 340, 90, 140, 45) * 0.6
    # Side hair
    v += em(x, y, 170, 250, 30, 80) * 0.55
    v += em(x, y, 510, 250, 30, 80) * 0.55

    # --- Forehead ---
    v += g(x, y, 340, 215, 100, 45) * 0.3
    v += em(x, y, 340, 230, 80, 35) * 0.2

    # --- Temples shadow ---
    v -= g(x, y, 200, 260, 25, 40) * 0.25
    v -= g(x, y, 480, 260, 25, 40) * 0.25

    # --- Eye region ---
    # Sockets
    v -= g(x, y, 285, 295, 38, 22) * 0.45
    v -= g(x, y, 395, 295, 38, 22) * 0.45

    # Eyes - white (sclera)
    v += ring(x, y, 285, 293, 0, 18, 3) * 0.8
    v += ring(x, y, 395, 293, 0, 18, 3) * 0.8

    # Iris
    v += g(x, y, 287, 293, 10, 10) * 0.85
    v += g(x, y, 393, 293, 10, 10) * 0.85

    # Pupil (darkest)
    v -= g(x, y, 287, 293, 4, 4) * 0.5
    v -= g(x, y, 393, 293, 4, 4) * 0.5

    # Eye highlight (catch light)
    v += g(x, y, 284, 290, 3, 3) * 0.95
    v += g(x, y, 390, 290, 3, 3) * 0.95

    # Eyelids
    v += em(x, y, 285, 278, 25, 6) * 0.5
    v += em(x, y, 395, 278, 25, 6) * 0.5
    v -= g(x, y, 285, 308, 22, 5) * 0.35
    v -= g(x, y, 395, 308, 22, 5) * 0.35

    # Lower lash line shadow
    v -= g(x, y, 285, 310, 20, 3) * 0.2
    v -= g(x, y, 395, 310, 20, 3) * 0.2

    # --- Eyebrows ---
    v += em(x, y, 285, 260, 35, 7) * 0.7
    v += em(x, y, 395, 260, 35, 7) * 0.7
    # Brow thickness variation
    v += g(x, y, 275, 257, 15, 4) * 0.3
    v += g(x, y, 405, 257, 15, 4) * 0.3

    # --- Nose ---
    # Bridge
    v += g(x, y, 340, 320, 10, 45) * 0.25
    # Nose sides (shadow)
    v -= g(x, y, 322, 345, 8, 35) * 0.25
    v -= g(x, y, 358, 345, 8, 35) * 0.25
    # Nose tip
    v += g(x, y, 340, 370, 16, 12) * 0.55
    # Nostrils
    v -= g(x, y, 328, 383, 7, 5) * 0.6
    v -= g(x, y, 352, 383, 7, 5) * 0.6
    # Nose shadow below
    v -= g(x, y, 340, 395, 20, 6) * 0.35
    # Nose highlight
    v += g(x, y, 340, 355, 6, 15) * 0.2

    # --- Philtrum ---
    v -= g(x, y, 340, 400, 5, 12) * 0.15

    # --- Mouth ---
    # Upper lip (Cupid's bow)
    v += em(x, y, 328, 416, 14, 6) * 0.45
    v += em(x, y, 352, 416, 14, 6) * 0.45
    v += g(x, y, 340, 413, 8, 4) * 0.3
    # Mouth line
    v += g(x, y, 340, 423, 35, 3) * 0.6
    # Lower lip
    v += em(x, y, 340, 433, 30, 10) * 0.4
    # Lip highlight
    v += g(x, y, 340, 430, 15, 5) * 0.15
    # Corners of mouth
    v -= g(x, y, 305, 422, 5, 5) * 0.3
    v -= g(x, y, 375, 422, 5, 5) * 0.3

    # --- Chin ---
    v += em(x, y, 340, 475, 35, 20) * 0.35
    # Chin dimple / shadow
    v += g(x, y, 340, 465, 8, 5) * 0.15
    # Chin shadow below
    v -= g(x, y, 340, 500, 45, 12) * 0.4

    # --- Jawline ---
    v -= g(x, y, 230, 460, 35, 50) * 0.3
    v -= g(x, y, 450, 460, 35, 50) * 0.3
    # Jaw contour highlight
    v += g(x, y, 250, 440, 30, 8) * 0.15
    v += g(x, y, 430, 440, 30, 8) * 0.15

    # --- Cheek shadows (contouring) ---
    v -= g(x, y, 225, 340, 30, 40) * 0.25
    v -= g(x, y, 455, 340, 30, 40) * 0.25
    # Cheekbone highlights
    v += g(x, y, 240, 310, 25, 15) * 0.15
    v += g(x, y, 440, 310, 25, 15) * 0.15

    # --- Neck ---
    v += em(x, y, 340, 540, 50, 45) * 0.45
    # Neck shadow
    v -= g(x, y, 340, 510, 40, 8) * 0.35
    # Neck sides
    v -= g(x, y, 285, 540, 15, 30) * 0.2
    v -= g(x, y, 395, 540, 15, 30) * 0.2

    # --- Ear (left) ---
    v += g(x, y, 155, 305, 12, 28) * 0.45
    v += em(x, y, 155, 305, 10, 22) * 0.3

    # --- Subtle noise for texture ---
    noise = random.uniform(-0.04, 0.04)
    v += noise

    v *= fade
    return max(0, min(1, v))

# Generate
dots = []
count = 0
for row in range(0, H, SPACING):
    for col in range(0, W, SPACING):
        jx = col + random.uniform(-0.8, 0.8)
        jy = row + random.uniform(-0.8, 0.8)
        intensity = compute(jx, jy)
        if intensity > 0.06:
            r = intensity * MAX_R
            o = 0.25 + intensity * 0.75
            dots.append(f'<circle cx="{col}" cy="{row}" r="{r:.2f}" fill="{FG}" opacity="{o:.2f}"/>')
            count += 1

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<rect width="{W}" height="{H}" fill="{BG}"/>
{"".join(dots)}
</svg>'''

with open("hero.svg", "w") as f:
    f.write(svg)

print(f"Done: {count} dots, {len(svg)} bytes")
