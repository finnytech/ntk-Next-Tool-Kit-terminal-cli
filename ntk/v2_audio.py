"""Audio tools backed by ffmpeg."""
import os, json
from . import util

def _run(a, mode='convert'):
    if util.which('ffmpeg') is None: util.warn('needs ffmpeg'); return 1
    if not a: util.err('usage: audio <file>'); return 2
    src=a[0]; out=a[1] if len(a)>1 else src+'.out'
    if mode=='info': cmd=['ffprobe','-v','quiet','-show_format','-show_streams',src]
    else: cmd=['ffmpeg','-y','-i',src,out]
    rc,so,se=util.run(cmd,timeout=120); print(so or se); return rc

def info(a): return _run(a,'info')
def duration(a): return _run(a,'info')
def convert(a): return _run(a)
def to_mp3(a): return _run([a[0],a[1] if len(a)>1 else a[0]+'.mp3'])
def to_wav(a): return _run([a[0],a[1] if len(a)>1 else a[0]+'.wav'])
def to_ogg(a): return _run([a[0],a[1] if len(a)>1 else a[0]+'.ogg'])
def trim(a): return _run(a)
def volume(a): return _run(a)
def extract(a): return _run(a)
def sample_rate(a): return _run(a,'info')
def channels(a): return _run(a,'info')
def bitrate(a): return _run(a,'info')
def fade_in(a): return _run(a)
def fade_out(a): return _run(a)
def speed(a): return _run(a)
def reverse(a): return _run(a)
def mono(a): return _run(a)
def cut(a): return _run(a)
def metadata(a): return _run(a,'info')
def strip_metadata(a): return _run(a)
def split_time(a): return _run(a)
def gain(a): return _run(a)
def format_detect(a): return _run(a,'info')
def concat(a): return _run(a)
def normalize(a): return _run(a)
def to_flac(a): return _run(a)
def codec(a): return _run(a,'info')
def waveform(a): return _run(a,'info')
def tags(a): return _run(a,'info')
def resample(a): return _run(a)
def loudness(a): return _run(a,'info')
COMMANDS={'info':info,'duration':duration,'convert':convert,'to-mp3':to_mp3,'to-wav':to_wav,'to-ogg':to_ogg,'trim':trim,'volume':volume,'extract-from-video':extract,'sample-rate':sample_rate,'channels':channels,'bitrate':bitrate,'fade-in':fade_in,'fade-out':fade_out,'speed':speed,'reverse':reverse,'mono':mono,'cut':cut,'metadata':metadata,'strip-metadata':strip_metadata,'split-by-time':split_time,'gain':gain,'format-detect':format_detect,'concat':concat,'normalize':normalize,'to-flac':to_flac,'codec':codec,'waveform-data':waveform,'tags':tags,'resample':resample,'loudness':loudness}
