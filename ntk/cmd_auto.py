"""Automation and convenience tools (ntk auto ...)."""
import json, os, platform, shutil, subprocess, time, urllib.parse, urllib.request, webbrowser, zipfile
from datetime import datetime
from pathlib import Path
from . import util
from .util import run, IS_WINDOWS

def alias(args):
    """Show or explain a shell alias."""
    if not args: util.err('usage: ntk auto alias <name> [command]'); return 2
    print((args[0]+'='+ ' '.join(args[1:])) if len(args)>1 else f'alias {args[0]} (define this in your shell)'); return 0

def backup(args):
    """Zip a folder with a timestamp."""
    if not args: util.err('usage: ntk auto backup <folder> [output.zip]'); return 2
    src=Path(args[0]); out=Path(args[1]) if len(args)>1 else Path(f'{src.name}-{datetime.now():%Y%m%d-%H%M%S}.zip')
    if not src.is_dir(): util.err('folder not found'); return 1
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
        for p in src.rglob('*'):
            if p.is_file(): z.write(p,p.relative_to(src.parent))
    print(out); return 0

def watch(args):
    """Run a command repeatedly every N seconds."""
    if len(args)<2: util.err('usage: ntk auto watch <seconds> <command> [args]'); return 2
    try: delay=float(args[0])
    except ValueError: util.err('seconds must be numeric'); return 2
    try:
        while True:
            rc,out,err=run(args[1:]); print(out,end=''); print(err,end=''); time.sleep(delay)
    except KeyboardInterrupt: print(); return 0

def notify(args):
    """Send a desktop notification or print it."""
    msg=' '.join(args) if args else 'NTK notification'
    if IS_WINDOWS:
        rc,out,err=run(['msg','*',msg]);
        if rc: print(msg)
    elif util.which('notify-send'): run(['notify-send','NTK',msg])
    else: print('[NOTIFY] '+msg)
    return 0

def macro(args):
    """Run a sequence of shell commands."""
    if not args: util.err('usage: ntk auto macro <command> [; command...]'); return 2
    for cmd in ' '.join(args).split(';'):
        rc,out,err=run(cmd.strip(),shell=True); print(out,end=''); print(err,end='')
        if rc: return rc
    return 0

def weather(args):
    """Fetch compact weather for a location."""
    if not args: util.err('usage: ntk auto weather <location>'); return 2
    try: print(urllib.request.urlopen('https://wttr.in/'+urllib.parse.quote(' '.join(args))+'?format=3',timeout=10).read().decode()); return 0
    except Exception as e: util.err(str(e)); return 1

def currency(args):
    """Fetch current exchange rates."""
    if len(args)<2: util.err('usage: ntk auto currency <from> <to> [amount]'); return 2
    try:
        data=json.loads(urllib.request.urlopen('https://open.er-api.com/v6/latest/'+args[0].upper(),timeout=10).read()); rate=data['rates'][args[1].upper()]; amount=float(args[2]) if len(args)>2 else 1; print(f'{amount:g} {args[0].upper()} = {amount*rate:.2f} {args[1].upper()}'); return 0
    except Exception as e: util.err(str(e)); return 1

def calculator(args):
    """Calculate percentages and simple interest."""
    if len(args)<3: util.err('usage: ntk auto calculator <percent|interest> values...'); return 2
    try:
        mode=args[0].lower(); vals=list(map(float,args[1:]))
        if mode in ('percent','percentage'): result=vals[0]*vals[1]/100
        elif mode=='interest': result=vals[0]*(1+vals[1]/100*vals[2]) if len(vals)>2 else vals[0]*vals[1]/100
        else: util.err('use percent or interest'); return 2
        print(result); return 0
    except ValueError: util.err('values must be numeric'); return 2

def reminder(args):
    """Wait minutes then print a reminder."""
    if len(args)<2: util.err('usage: ntk auto reminder <minutes> <message>'); return 2
    try: minutes=float(args[0])
    except ValueError: util.err('minutes must be numeric'); return 2
    time.sleep(max(0,minutes*60)); return notify(args[1:])

def todo_list(args):
    """Add, list or complete local todos."""
    fn=Path('.ntk-todo.json')
    try: items=json.loads(fn.read_text()) if fn.exists() else []
    except Exception: items=[]
    action=args[0] if args else 'list'
    if action=='add' and len(args)>1: items.append({'text':' '.join(args[1:]),'done':False})
    elif action=='done' and len(args)>1 and args[1].isdigit() and 0<=int(args[1])-1<len(items): items[int(args[1])-1]['done']=True
    elif action!='list': util.err('usage: ntk auto todo-list [add text|done number|list]'); return 2
    fn.write_text(json.dumps(items,indent=2))
    for i,x in enumerate(items,1): print(f"{i}. {'[x]' if x['done'] else '[ ]'} {x['text']}")
    return 0

def clip_copy(args):
    """Copy text to the system clipboard."""
    text=' '.join(args)
    if IS_WINDOWS: rc,_,_=run(['clip'],shell=False); print(text); return 0
    cmd=['xclip','-selection','clipboard'] if util.which('xclip') else ['xsel','--clipboard','--input']
    if not util.which(cmd[0]): util.warn('needs xclip or xsel'); return 1
    p=subprocess.run(cmd,input=text,text=True); return p.returncode

def clip_paste(args):
    """Print text from the system clipboard."""
    if IS_WINDOWS: rc,out,err=run(['powershell','-NoProfile','-Command','Get-Clipboard']); print(out,end=''); return rc
    cmd=['xclip','-selection','clipboard','-o'] if util.which('xclip') else ['xsel','--clipboard','--output']
    if not util.which(cmd[0]): util.warn('needs xclip or xsel'); return 1
    rc,out,err=run(cmd); print(out,end=''); return rc

def open_cmd(args):
    """Open a URL or file with the default application."""
    if not args: util.err('usage: ntk auto open <url-or-path>'); return 2
    target=' '.join(args)
    try:
        if IS_WINDOWS: os.startfile(target)
        elif util.which('xdg-open'): subprocess.Popen(['xdg-open',target],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        else: webbrowser.open(target)
        return 0
    except OSError as e: util.err(str(e)); return 1

def search_web(args):
    """Open a web search for terms."""
    if not args: util.err('usage: ntk auto search-web <query>'); return 2
    webbrowser.open('https://www.google.com/search?q='+urllib.parse.quote(' '.join(args))); return 0

def update(args):
    """Show the current NTK update note."""
    util.info('NTK is running from the current workspace. Check your project source for updates.'); return 0

COMMANDS={'alias':alias,'backup':backup,'watch':watch,'notify':notify,'macro':macro,'weather':weather,'currency':currency,'calculator':calculator,'reminder':reminder,'todo-list':todo_list,'clip-copy':clip_copy,'clip-paste':clip_paste,'open':open_cmd,'search-web':search_web,'update':update}
