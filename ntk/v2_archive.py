"""Archive tools."""
import os, zipfile, tarfile, gzip, shutil, base64, hashlib, time
from . import util

def _need(a,n=1):
    if len(a)<n: raise ValueError()

def zip_cmd(a):
    try:
        _need(a,2); src,dest=a[0],a[1]
        with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
            if os.path.isdir(src):
                for r,_,fs in os.walk(src):
                    for f in fs: z.write(os.path.join(r,f),os.path.relpath(os.path.join(r,f),os.path.dirname(src)))
            else: z.write(src,os.path.basename(src))
        return 0
    except Exception: util.err('usage: zip <src> <dest>'); return 2
def unzip(a):
    try: _need(a,2); zipfile.ZipFile(a[0]).extractall(a[1]); return 0
    except Exception: return 2
def zip_list(a):
    try:
        with zipfile.ZipFile(a[0]) as z:
            for x in z.infolist(): print(x.filename, x.file_size)
        return 0
    except Exception: return 2
def tar_cmd(a):
    try:
        _need(a,2)
        with tarfile.open(a[1],'w') as t: t.add(a[0],arcname=os.path.basename(a[0]))
        return 0
    except Exception: return 2
def untar(a):
    try: _need(a,2); tarfile.open(a[0]).extractall(a[1]); return 0
    except Exception: return 2
def tar_list(a):
    try:
        for x in tarfile.open(a[0]).getmembers(): print(x.name,x.size)
        return 0
    except Exception: return 2
def gzip_cmd(a):
    try:
        p=a[0]; out=p+'.gz'
        with open(p,'rb') as i,gzip.open(out,'wb') as o: shutil.copyfileobj(i,o)
        return 0
    except Exception: return 2
def gunzip(a):
    try:
        p=a[0]; out=p[:-3] if p.endswith('.gz') else p+'.out'
        with gzip.open(p,'rb') as i,open(out,'wb') as o: shutil.copyfileobj(i,o)
        return 0
    except Exception: return 2
def targz(a):
    try:
        with tarfile.open(a[1],'w:gz') as t: t.add(a[0],arcname=os.path.basename(a[0]))
        return 0
    except Exception: return 2
def zip_add(a):
    try:
        with zipfile.ZipFile(a[0],'a',zipfile.ZIP_DEFLATED) as z: z.write(a[1],os.path.basename(a[1]))
        return 0
    except Exception: return 2
def zip_one(a):
    try: zipfile.ZipFile(a[0]).extract(a[1],a[2] if len(a)>2 else '.'); return 0
    except Exception: return 2
def backup(a):
    try: return zip_cmd([a[0],a[0].rstrip('/\\')+'-'+time.strftime('%Y%m%d-%H%M%S')+'.zip'])
    except Exception: return 2
def zsize(a):
    try: print(util.human_bytes(os.path.getsize(a[0]))); return 0
    except Exception: return 2
def ztest(a):
    try: print(zipfile.ZipFile(a[0]).testzip() or 'OK'); return 0
    except Exception: return 2
def ratio(a):
    try: print(os.path.getsize(a[0])); return 0
    except Exception: return 2
def folder_zip(a): return zip_cmd(a)
def zcount(a):
    try: print(len(zipfile.ZipFile(a[0]).infolist())); return 0
    except Exception: return 2
def largest_zip(a):
    try: print(max(zipfile.ZipFile(a[0]).infolist(),key=lambda x:x.file_size).filename); return 0
    except Exception: return 2
def tarsize(a): return zsize(a)
def extract(a):
    try:
        p,d=a[0],a[1]
        if zipfile.is_zipfile(p): return unzip([p,d])
        if tarfile.is_tarfile(p): return untar([p,d])
        return gunzip([p])
    except Exception: return 2
def split_file(a):
    try:
        p,mb=a[0],int(a[1]); size=mb*1048576
        with open(p,'rb') as f:
            i=0
            while True:
                b=f.read(size)
                if not b: break
                with open(f'{p}.part{i:04d}','wb') as o:o.write(b)
                i+=1
        return 0
    except Exception:return 2
def join_files(a):
    try:
        pre,d=a[0],a[1]
        with open(d,'wb') as o:
            for p in sorted(x for x in os.listdir('.') if x.startswith(pre)): o.write(open(p,'rb').read())
        return 0
    except Exception:return 2
def b64e(a):
    try: print(base64.b64encode(open(a[0],'rb').read()).decode()); return 0
    except Exception:return 2
def b64d(a):
    try: open(a[1],'wb').write(base64.b64decode(open(a[0],'rb').read())); return 0
    except Exception:return 2
def checksum(a):
    try: print(hashlib.sha256(open(a[0],'rb').read()).hexdigest()); return 0
    except Exception:return 2
def supported(a): print('zip tar gz'); return 0
def comment(a):
    try: print((zipfile.ZipFile(a[0]).comment or b'').decode()); return 0
    except Exception:return 2
def flatten(a):
    try:
        with zipfile.ZipFile(a[0]) as z,zipfile.ZipFile(a[1],'w') as o:
            for x in z.infolist():
                if not x.is_dir(): o.writestr(os.path.basename(x.filename),z.read(x))
        return 0
    except Exception:return 2
def gzsize(a): return zsize(a)
def untargz(a): return untar(a)
def zinfo(a): return zip_list(a)
COMMANDS={'zip':zip_cmd,'unzip':unzip,'zip-list':zip_list,'tar':tar_cmd,'untar':untar,'tar-list':tar_list,'gzip':gzip_cmd,'gunzip':gunzip,'targz':targz,'zip-add':zip_add,'zip-extract-one':zip_one,'backup':backup,'zip-size':zsize,'zip-test':ztest,'compress-ratio':ratio,'folder-to-zip':folder_zip,'zip-count':zcount,'largest-in-zip':largest_zip,'tar-size':tarsize,'extract':extract,'split-file':split_file,'join-files':join_files,'b64-encode-file':b64e,'b64-decode-file':b64d,'checksum-archive':checksum,'list-supported':supported,'zip-comment':comment,'zip-flatten':flatten,'gz-size':gzsize,'untargz':untargz,'zip-info':zinfo}
