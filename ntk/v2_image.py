"""Image tools using Pillow when available."""
import os
from . import util

def _pil():
    try:
        from PIL import Image, ImageEnhance, ImageFilter, ImageOps
        return Image,ImageEnhance,ImageFilter,ImageOps
    except ImportError:
        util.warn('needs Pillow: pip install Pillow'); return None

def _open(a):
    if not a: raise ValueError()
    p=_pil()
    if not p: return None,None
    return p,p[0].open(a[0])
def info(a):
    p,i=_open(a)
    if i is None:return 1
    print(i.format,i.size,i.mode); return 0
def dimensions(a): return info(a)
def format_detect(a): return info(a)
def _save(a,fn):
    p,i=_open(a)
    if i is None:return 1
    out=a[1] if len(a)>1 else os.path.splitext(a[0])[0]+fn
    i.save(out); print(out); return 0
def resize(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        out=a[3] if len(a)>3 else os.path.splitext(a[0])[0]+'-resize.png'; i.resize((int(a[1]),int(a[2]))).save(out); print(out); return 0
    except Exception: return 2
def scale(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        f=float(a[1])/100; out=a[2] if len(a)>2 else os.path.splitext(a[0])[0]+'-scale.png'; i.resize((max(1,int(i.width*f)),max(1,int(i.height*f)))).save(out); print(out); return 0
    except Exception:return 2
def convert(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        fmt=a[1].upper(); out=a[2] if len(a)>2 else os.path.splitext(a[0])[0]+'.'+a[1].lower(); i.convert('RGB' if fmt in {'JPG','JPEG'} else i.mode).save(out,fmt); print(out); return 0
    except Exception:return 2
def thumbnail(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        i.thumbnail((int(a[1]),int(a[1]))); i.save(a[2] if len(a)>2 else a[0]); return 0
    except Exception:return 2
def rotate(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        i.rotate(float(a[1]),expand=True).save(a[2] if len(a)>2 else a[0]); return 0
    except Exception:return 2
def flip(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        i.transpose(p[3].FLIP_LEFT_RIGHT if a[1]=='h' else p[3].FLIP_TOP_BOTTOM).save(a[2] if len(a)>2 else a[0]); return 0
    except Exception:return 2
def grayscale(a): return _save_op(a,lambda p,i:p.convert('L'))
def invert(a):
    p,i=_open(a)
    if i is None:return 1
    return _save_op(a,lambda x,y:p[3].invert(y.convert('RGB')))
def _save_op(a,fn):
    try:
        p,i=_open(a)
        if i is None:return 1
        i2=fn(p,i); i2.save(a[1] if len(a)>1 else a[0]); return 0
    except Exception:return 2
def crop(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        i.crop(tuple(map(int,a[1:5]))).save(a[5] if len(a)>5 else a[0]); return 0
    except Exception:return 2
def blur(a): return _save_op(a,lambda p,i:i.filter(p[2].GaussianBlur(float(a[1]))))
def sharpen(a): return _save_op(a,lambda p,i:i.filter(p[2].SHARPEN))
def brightness(a): return _save_op(a,lambda p,i:p[1].Brightness(i).enhance(float(a[1])))
def contrast(a): return _save_op(a,lambda p,i:p[1].Contrast(i).enhance(float(a[1])))
def to_jpg(a): return convert([a[0],'jpg']+a[1:])
def to_png(a): return convert([a[0],'png']+a[1:])
def to_webp(a): return convert([a[0],'webp']+a[1:])
def dominant(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        print(i.resize((1,1)).getpixel((0,0))); return 0
    except Exception:return 2
def palette(a): return dominant(a)
def exif(a): return info(a)
def strip_exif(a): return convert(a)
def border(a):
    try:
        p,i=_open(a)
        if i is None:return 1
        p[3].expand(i,int(a[1]),fill='black').save(a[2] if len(a)>2 else a[0]); return 0
    except Exception:return 2
def pad(a): return border(a)
def fit(a): return resize(a)
def compress(a): return convert(a)
def batch_convert(a):
    try:
        for f in os.listdir(a[0]):
            p=os.path.join(a[0],f)
            if os.path.isfile(p): convert([p,a[1]])
        return 0
    except Exception:return 2
def pixelate(a): return thumbnail(a)
def mirror(a): return flip([a[0],'h']+a[1:])
def histogram(a):
    p,i=_open(a)
    if i is None:return 1
    print(i.histogram()); return 0
def largest_image(a):
    try:
        best=max((os.path.join(a[0],f) for f in os.listdir(a[0])),key=os.path.getsize); print(best); return 0
    except Exception:return 2
COMMANDS={'info':info,'resize':resize,'scale':scale,'convert':convert,'thumbnail':thumbnail,'rotate':rotate,'flip':flip,'grayscale':grayscale,'crop':crop,'blur':blur,'sharpen':sharpen,'brightness':brightness,'contrast':contrast,'invert':invert,'to-jpg':to_jpg,'to-png':to_png,'to-webp':to_webp,'dimensions':dimensions,'dominant-color':dominant,'palette':palette,'exif':exif,'strip-exif':strip_exif,'border':border,'pad':pad,'fit':fit,'compress':compress,'batch-convert':batch_convert,'pixelate':pixelate,'mirror':mirror,'histogram':histogram,'format-detect':format_detect,'largest-image':largest_image}
