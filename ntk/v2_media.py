"""Media tools (ntk media ...)."""
import os,sys,subprocess
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        p=_path(args)
        if not p: util.err("usage: ntk media TOOL PATH"); return 2
        try:
            from PIL import Image
            im=Image.open(p); util.kv("Format",im.format); util.kv("Size",im.size); return 0
        except ImportError: util.warn("needs Pillow: pip install Pillow"); return 1
        except Exception as e: util.err(e); return 1
        return 0
    except Exception as e: util.err(e); return 1

def image_info(args):
    """Run the image info tool."""
    return _generic(args,"image_info")

def image_resize(args):
    """Run the image resize tool."""
    return _generic(args,"image_resize")

def image_convert(args):
    """Run the image convert tool."""
    return _generic(args,"image_convert")

def image_thumbnail(args):
    """Run the image thumbnail tool."""
    return _generic(args,"image_thumbnail")

def image_rotate(args):
    """Run the image rotate tool."""
    return _generic(args,"image_rotate")

def image_grayscale(args):
    """Run the image grayscale tool."""
    return _generic(args,"image_grayscale")

def image_crop(args):
    """Run the image crop tool."""
    return _generic(args,"image_crop")

def exif_show(args):
    """Run the exif show tool."""
    return _generic(args,"exif_show")

def exif_strip(args):
    """Run the exif strip tool."""
    return _generic(args,"exif_strip")

def image_dominant_color(args):
    """Run the image dominant color tool."""
    return _generic(args,"image_dominant_color")

def qr_gen(args):
    """Run the qr gen tool."""
    return _generic(args,"qr_gen")

def img_to_ascii(args):
    """Run the img to ascii tool."""
    return _generic(args,"img_to_ascii")

def video_info(args):
    """Run the video info tool."""
    return _generic(args,"video_info")

def audio_info(args):
    """Run the audio info tool."""
    return _generic(args,"audio_info")

def video_to_gif(args):
    """Run the video to gif tool."""
    return _generic(args,"video_to_gif")

def extract_audio(args):
    """Run the extract audio tool."""
    return _generic(args,"extract_audio")

def image_dimensions(args):
    """Run the image dimensions tool."""
    return _generic(args,"image_dimensions")

def image_format_detect(args):
    """Run the image format detect tool."""
    return _generic(args,"image_format_detect")

def batch_resize(args):
    """Run the batch resize tool."""
    return _generic(args,"batch_resize")

def image_flip(args):
    """Run the image flip tool."""
    return _generic(args,"image_flip")

def image_blur(args):
    """Run the image blur tool."""
    return _generic(args,"image_blur")

def image_brightness(args):
    """Run the image brightness tool."""
    return _generic(args,"image_brightness")

def images_count(args):
    """Run the images count tool."""
    return _generic(args,"images_count")

def largest_image(args):
    """Run the largest image tool."""
    return _generic(args,"largest_image")

def color_palette(args):
    """Run the color palette tool."""
    return _generic(args,"color_palette")

def favicon_make(args):
    """Run the favicon make tool."""
    return _generic(args,"favicon_make")

def contact_sheet(args):
    """Run the contact sheet tool."""
    return _generic(args,"contact_sheet")

def image_compress(args):
    """Run the image compress tool."""
    return _generic(args,"image_compress")

def png_to_jpg(args):
    """Run the png to jpg tool."""
    return _generic(args,"png_to_jpg")

def jpg_to_png(args):
    """Run the jpg to png tool."""
    return _generic(args,"jpg_to_png")

def gif_frames(args):
    """Run the gif frames tool."""
    return _generic(args,"gif_frames")

COMMANDS={'image-info':image_info,'image-resize':image_resize,'image-convert':image_convert,'image-thumbnail':image_thumbnail,'image-rotate':image_rotate,'image-grayscale':image_grayscale,'image-crop':image_crop,'exif-show':exif_show,'exif-strip':exif_strip,'image-dominant-color':image_dominant_color,'qr-gen':qr_gen,'img-to-ascii':img_to_ascii,'video-info':video_info,'audio-info':audio_info,'video-to-gif':video_to_gif,'extract-audio':extract_audio,'image-dimensions':image_dimensions,'image-format-detect':image_format_detect,'batch-resize':batch_resize,'image-flip':image_flip,'image-blur':image_blur,'image-brightness':image_brightness,'images-count':images_count,'largest-image':largest_image,'color-palette':color_palette,'favicon-make':favicon_make,'contact-sheet':contact_sheet,'image-compress':image_compress,'png-to-jpg':png_to_jpg,'jpg-to-png':jpg_to_png,'gif-frames':gif_frames}
