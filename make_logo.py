"""Generate the NTK logo (PNG) and a multi-size Windows .ico, using Pillow only."""
import os
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
OUT_PNG = "assets/ntk_logo.png"
OUT_ICO = "assets/ntk.ico"


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def rounded_gradient(size, c_top, c_bottom, radius_frac=0.22):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    grad = Image.new("RGB", (size, size))
    px = grad.load()
    for y in range(size):
        row = lerp(c_top, c_bottom, y / size)
        for x in range(size):
            px[x, y] = row
    # rounded mask
    mask = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(mask)
    r = int(size * radius_frac)
    md.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=255)
    img.paste(grad, (0, 0), mask)
    return img


def load_font(size, bold=True):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_glow(base, draw_fn, glow_color, blur=18, passes=3):
    from PIL import ImageFilter
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    draw_fn(d)
    glow = layer.filter(ImageFilter.GaussianBlur(blur))
    for _ in range(passes):
        base.alpha_composite(glow)
    base.alpha_composite(layer)


def main():
    os.makedirs("assets", exist_ok=True)
    # Palette: deep blue -> charcoal background, electric cyan accents
    bg = rounded_gradient(SIZE, (18, 26, 44), (10, 14, 24))
    draw = ImageDraw.Draw(bg)

    # Inner terminal window panel
    pad = int(SIZE * 0.16)
    top = int(SIZE * 0.24)
    panel = [pad, top, SIZE - pad, SIZE - int(SIZE * 0.20)]
    pr = int(SIZE * 0.05)
    draw.rounded_rectangle(panel, radius=pr, fill=(13, 20, 34), outline=(40, 220, 235), width=6)

    # Title bar dots
    dot_y = top + int(SIZE * 0.045)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        cx = pad + int(SIZE * 0.055) + i * int(SIZE * 0.05)
        draw.ellipse([cx - 12, dot_y - 12, cx + 12, dot_y + 12], fill=c)

    # ">_" prompt glowing cyan
    mono = load_font(int(SIZE * 0.16))
    cyan = (40, 220, 235, 255)

    def draw_prompt(d):
        d.text((pad + int(SIZE * 0.06), top + int(SIZE * 0.13)), ">_", font=mono, fill=cyan)
    draw_glow(bg, draw_prompt, cyan, blur=16, passes=2)

    # NTK monogram, big, bottom
    big = load_font(int(SIZE * 0.20))
    text = "NTK"
    bbox = draw.textbbox((0, 0), text, font=big)
    tw = bbox[2] - bbox[0]
    tx = (SIZE - tw) // 2
    ty = SIZE - int(SIZE * 0.205)

    def draw_ntk(d):
        d.text((tx, ty), text, font=big, fill=(235, 245, 255, 255))
    draw_glow(bg, draw_ntk, (60, 160, 255), blur=12, passes=2)

    bg.save(OUT_PNG)
    print("wrote", OUT_PNG)

    # ICO with multiple sizes
    ico_sizes = [16, 24, 32, 48, 64, 128, 256]
    bg.save(OUT_ICO, sizes=[(s, s) for s in ico_sizes])
    print("wrote", OUT_ICO)


if __name__ == "__main__":
    main()
