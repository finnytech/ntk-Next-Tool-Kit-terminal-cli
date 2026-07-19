"""Media & asset tools (ntk media ...)."""
import os
import base64
from . import util
from .util import col, C, run, which

try:
    from PIL import Image
except ImportError:
    Image = None


def _need_pil():
    if Image is None:
        util.warn("this tool needs Pillow: pip install pillow")
        return False
    return True


def _need_ffmpeg():
    if not which("ffmpeg"):
        util.warn("this tool needs ffmpeg on PATH")
        return False
    return True


def exif_read(args):
    """Read EXIF metadata from an image."""
    if not args:
        util.err("usage: ntk media exif-read <image>")
        return 2
    if not _need_pil():
        return 1
    try:
        img = Image.open(args[0])
        exif = img.getexif()
        if not exif:
            util.info("no EXIF data")
            return 0
        from PIL.ExifTags import TAGS, GPSTAGS
        util.header("EXIF")
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                gps = {GPSTAGS.get(k, k): v for k, v in value.items()} if hasattr(value, "items") else value
                util.kv("GPS", gps)
            else:
                util.kv(tag, str(value)[:60])
    except Exception as e:
        util.err(e)
        return 1
    return 0


def exif_strip(args):
    """Remove all EXIF data from an image."""
    if not args:
        util.err("usage: ntk media exif-strip <image> [out]")
        return 2
    if not _need_pil():
        return 1
    src = args[0]
    out = args[1] if len(args) > 1 else src.rsplit(".", 1)[0] + "_clean." + src.rsplit(".", 1)[1]
    img = Image.open(src)
    data = list(img.getdata())
    clean = Image.new(img.mode, img.size)
    clean.putdata(data)
    clean.save(out)
    util.ok(f"saved without EXIF -> {out}")
    return 0


def img_resize(args):
    """Resize an image (WIDTHxHEIGHT)."""
    if len(args) < 2:
        util.err("usage: ntk media img-resize <image> <WxH> [out]")
        return 2
    if not _need_pil():
        return 1
    src, dim = args[0], args[1]
    w, h = (int(x) for x in dim.lower().split("x"))
    out = args[2] if len(args) > 2 else src.rsplit(".", 1)[0] + f"_{w}x{h}." + src.rsplit(".", 1)[1]
    Image.open(src).resize((w, h)).save(out)
    util.ok(f"resized -> {out}")
    return 0


def img_convert(args):
    """Convert image format (by output extension)."""
    if len(args) < 2:
        util.err("usage: ntk media img-convert <in> <out.ext>")
        return 2
    if not _need_pil():
        return 1
    img = Image.open(args[0])
    if args[1].lower().endswith((".jpg", ".jpeg")) and img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save(args[1])
    util.ok(f"converted -> {args[1]}")
    return 0


def gif_gen(args):
    """Create a GIF from a video or image sequence."""
    if not args:
        util.err("usage: ntk media gif-gen <video|glob> [out.gif]")
        return 2
    if not _need_ffmpeg():
        return 1
    out = args[1] if len(args) > 1 else "out.gif"
    rc, o, e = run(["ffmpeg", "-y", "-i", args[0], "-vf", "fps=10,scale=480:-1:flags=lanczos", out])
    print(o or e)
    return rc


def video_mute(args):
    """Remove the audio track from a video."""
    if not args:
        util.err("usage: ntk media video-mute <video> [out]")
        return 2
    if not _need_ffmpeg():
        return 1
    out = args[1] if len(args) > 1 else "muted_" + os.path.basename(args[0])
    rc, o, e = run(["ffmpeg", "-y", "-i", args[0], "-c", "copy", "-an", out])
    print(o or e)
    return rc


def audio_extract(args):
    """Extract audio from a video (mp3/aac)."""
    if not args:
        util.err("usage: ntk media audio-extract <video> [out.mp3]")
        return 2
    if not _need_ffmpeg():
        return 1
    out = args[1] if len(args) > 1 else args[0].rsplit(".", 1)[0] + ".mp3"
    rc, o, e = run(["ffmpeg", "-y", "-i", args[0], "-q:a", "0", "-map", "a", out])
    print(o or e)
    return rc


def audio_convert(args):
    """Convert audio format (by output extension)."""
    if len(args) < 2:
        util.err("usage: ntk media audio-convert <in> <out.ext>")
        return 2
    if not _need_ffmpeg():
        return 1
    rc, o, e = run(["ffmpeg", "-y", "-i", args[0], args[1]])
    print(o or e)
    return rc


def img_color(args):
    """Show dominant HEX colors in an image."""
    if not args:
        util.err("usage: ntk media img-color <image>")
        return 2
    if not _need_pil():
        return 1
    img = Image.open(args[0]).convert("RGB").resize((100, 100))
    colors = img.getcolors(10000) or []
    colors.sort(reverse=True)
    util.header("Dominant colors")
    for count, (r, g, b) in colors[:8]:
        hexc = f"#{r:02x}{g:02x}{b:02x}"
        swatch = f"\033[48;2;{r};{g};{b}m      \033[0m"
        print(f"  {swatch} {hexc}  ({count}px)")
    return 0


def compress_video(args):
    """Compress a video (keep quality)."""
    if not args:
        util.err("usage: ntk media compress-video <video> [out] [crf=28]")
        return 2
    if not _need_ffmpeg():
        return 1
    out = args[1] if len(args) > 1 else "compressed_" + os.path.basename(args[0])
    crf = args[2] if len(args) > 2 else "28"
    rc, o, e = run(["ffmpeg", "-y", "-i", args[0], "-vcodec", "libx264", "-crf", crf, out])
    print(o or e)
    return rc


def waveform(args):
    """ASCII waveform of an audio file."""
    if not args:
        util.err("usage: ntk media waveform <audio>")
        return 2
    if not _need_ffmpeg():
        return 1
    import tempfile
    import wave
    tmp = tempfile.mktemp(suffix=".wav")
    run(["ffmpeg", "-y", "-i", args[0], "-ac", "1", "-ar", "8000", tmp])
    try:
        w = wave.open(tmp, "rb")
        frames = w.readframes(w.getnframes())
        import struct
        samples = struct.unpack("<%dh" % (len(frames) // 2), frames)
        step = max(1, len(samples) // 100)
        util.header("Waveform")
        for i in range(0, len(samples), step):
            amp = abs(samples[i]) / 32768
            print("  " + col("#" * int(amp * 50), C.CYAN))
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    return 0


def icon_gen(args):
    """Generate app/web icons (favicon sizes)."""
    if not args:
        util.err("usage: ntk media icon-gen <image>")
        return 2
    if not _need_pil():
        return 1
    img = Image.open(args[0]).convert("RGBA")
    sizes = [16, 32, 48, 64, 128, 180, 192, 512]
    outdir = "icons"
    os.makedirs(outdir, exist_ok=True)
    for s in sizes:
        img.resize((s, s)).save(os.path.join(outdir, f"icon-{s}.png"))
    img.resize((32, 32)).save(os.path.join(outdir, "favicon.ico"),
                              sizes=[(16, 16), (32, 32), (48, 48)])
    util.ok(f"icons written to ./{outdir}/")
    return 0


def pdf_merge(args):
    """Merge multiple PDFs into one."""
    if len(args) < 2:
        util.err("usage: ntk media pdf-merge <out.pdf> <in1.pdf> <in2.pdf> ...")
        return 2
    try:
        from pypdf import PdfWriter
    except ImportError:
        try:
            from PyPDF2 import PdfMerger as _M
        except ImportError:
            util.warn("needs pypdf: pip install pypdf")
            return 1
        m = _M()
        for p in args[1:]:
            m.append(p)
        m.write(args[0])
        util.ok(f"merged -> {args[0]}")
        return 0
    w = PdfWriter()
    for p in args[1:]:
        w.append(p)
    with open(args[0], "wb") as f:
        w.write(f)
    util.ok(f"merged -> {args[0]}")
    return 0


def pdf_split(args):
    """Split a PDF into single pages."""
    if not args:
        util.err("usage: ntk media pdf-split <in.pdf>")
        return 2
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        util.warn("needs pypdf: pip install pypdf")
        return 1
    r = PdfReader(args[0])
    base = args[0].rsplit(".", 1)[0]
    for i, page in enumerate(r.pages):
        w = PdfWriter()
        w.add_page(page)
        with open(f"{base}_p{i+1}.pdf", "wb") as f:
            w.write(f)
    util.ok(f"split into {len(r.pages)} pages")
    return 0


def pdf_pages(args):
    """Count the pages of a PDF."""
    if not args:
        util.err("usage: ntk media pdf-pages <in.pdf>")
        return 2
    try:
        from pypdf import PdfReader
    except ImportError:
        util.warn("needs pypdf: pip install pypdf")
        return 1
    print(f"  {len(PdfReader(args[0]).pages)} pages")
    return 0


def ocr(args):
    """Read text from an image (OCR)."""
    if not args:
        util.err("usage: ntk media ocr <image>")
        return 2
    try:
        import pytesseract
    except ImportError:
        util.warn("needs pytesseract + tesseract binary: pip install pytesseract")
        return 1
    if not _need_pil():
        return 1
    text = pytesseract.image_to_string(Image.open(args[0]))
    print(text)
    return 0


def qrcode(args):
    """Create a QR code from text/URL."""
    if not args:
        util.err("usage: ntk media qrcode <text> [out.png]")
        return 2
    try:
        import qrcode as _qr
    except ImportError:
        util.warn("needs qrcode: pip install qrcode[pil]")
        return 1
    qr = _qr.QRCode()
    qr.add_data(" ".join(a for a in args if not a.endswith(".png")))
    qr.make()
    out = next((a for a in args if a.endswith(".png")), None)
    if out:
        qr.make_image().save(out)
        util.ok(f"saved -> {out}")
    else:
        qr.print_ascii(invert=True)
    return 0


def qrcode_read(args):
    """Decode a QR code from an image."""
    if not args:
        util.err("usage: ntk media qrcode-read <image>")
        return 2
    try:
        from pyzbar.pyzbar import decode
    except ImportError:
        util.warn("needs pyzbar: pip install pyzbar")
        return 1
    if not _need_pil():
        return 1
    for d in decode(Image.open(args[0])):
        print("  " + d.data.decode("utf-8", "replace"))
    return 0


def ascii_art(args):
    """Turn an image into colored ASCII art."""
    if not args:
        util.err("usage: ntk media ascii-art <image> [width]")
        return 2
    if not _need_pil():
        return 1
    width = int(args[1]) if len(args) > 1 else 80
    img = Image.open(args[0]).convert("RGB")
    ratio = img.height / img.width
    height = int(width * ratio * 0.5)
    img = img.resize((width, height))
    chars = " .:-=+*#%@"
    out = []
    for y in range(height):
        line = []
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            ch = chars[int(lum * (len(chars) - 1))]
            line.append(f"\033[38;2;{r};{g};{b}m{ch}\033[0m")
        out.append("".join(line))
    print("\n".join(out))
    return 0


def watermark(args):
    """Add a text watermark to an image."""
    if len(args) < 2:
        util.err('usage: ntk media watermark <image> "text" [out]')
        return 2
    if not _need_pil():
        return 1
    from PIL import ImageDraw, ImageFont
    img = Image.open(args[0]).convert("RGBA")
    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    try:
        font = ImageFont.truetype("arial.ttf", max(20, img.width // 20))
    except Exception:
        font = ImageFont.load_default()
    draw.text((img.width // 20, img.height - img.height // 8), args[1],
              fill=(255, 255, 255, 128), font=font)
    out = args[2] if len(args) > 2 else "watermarked_" + os.path.basename(args[0])
    Image.alpha_composite(img, txt).convert("RGB").save(out)
    util.ok(f"saved -> {out}")
    return 0


COMMANDS = {
    "exif-read": exif_read, "exif-strip": exif_strip, "img-resize": img_resize,
    "img-convert": img_convert, "gif-gen": gif_gen, "video-mute": video_mute,
    "audio-extract": audio_extract, "audio-convert": audio_convert,
    "img-color": img_color, "compress-video": compress_video, "waveform": waveform,
    "icon-gen": icon_gen, "pdf-merge": pdf_merge, "pdf-split": pdf_split,
    "pdf-pages": pdf_pages, "ocr": ocr, "qrcode": qrcode, "qrcode-read": qrcode_read,
    "ascii-art": ascii_art, "watermark": watermark,
}
