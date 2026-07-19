"""Small productivity tools."""
import os,sys,random,uuid,base64,datetime,math,secrets,string
from . import util
D=os.path.expanduser('~/.ntk'); os.makedirs(D,exist_ok=True)
N=os.path.join(D,'notes.txt'); T=os.path.join(D,'todos.txt')
def _print(x): print(x); return 0
def note_add(a): open(N,'a').write(' '.join(a)+'\n'); return 0
def note_list(a): return _print(open(N).read() if os.path.exists(N) else '')
def note_clear(a):
 if '--yes' not in a: return 2
 open(N,'w').close(); return 0
def todo_add(a): open(T,'a').write(' '.join(a)+'\n'); return 0
def todo_list(a): return _print(open(T).read() if os.path.exists(T) else '')
def todo_done(a):
 try:
  ls=open(T).readlines(); ls.pop(int(a[0])-1); open(T,'w').writelines(ls); return 0
 except Exception:return 2
def todo_clear(a):
 if '--yes' not in a:return 2
 open(T,'w').close(); return 0
def calc(a):
 try: return _print(eval(' '.join(a),{'__builtins__':{}},{k:getattr(math,k) for k in dir(math) if not k.startswith('_')}))
 except Exception:return 2
def timer(a):
 if not sys.stdin.isatty(): return 2
 try: import time; time.sleep(min(int(a[0]),3600)); print('done'); return 0
 except Exception:return 2
def stopwatch(a): return 2 if not sys.stdin.isatty() else _print('stopwatch')
def pomodoro(a): return 2 if not sys.stdin.isatty() else _print('pomodoro')
def word_count(a): return _print(len(' '.join(a).split()))
def char_count(a): return _print(len(' '.join(a)))
def quote(a): return _print(random.choice(['Start small.','Keep going.','Make it clear.']))
def coin(a): return _print(random.choice(['heads','tails']))
def dice(a): return roll(a)
def random_pick(a): return _print(random.choice(' '.join(a).split(',')))
def password(a):
 try:return _print(''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(int(a[0]))))
 except Exception:return 2
def uid(a): return _print(uuid.uuid4())
def b64e(a): return _print(base64.b64encode(' '.join(a).encode()).decode())
def b64d(a):
 try:return _print(base64.b64decode(''.join(a)).decode())
 except Exception:return 2
def banner(a): return _print('\n'.join(' '.join(x*2 for x in ' '.join(a))))
def countdown(a):
 try:return _print((datetime.date.fromisoformat(a[0])-datetime.date.today()).days)
 except Exception:return 2
def age(a):
 try:return _print((datetime.date.today()-datetime.date.fromisoformat(a[0])).days//365)
 except Exception:return 2
def color(a): return _print('#%06x'%random.randrange(1<<24))
def motivate(a): return quote(a)
def roll(a):
 try:
  n,m=map(int,a[0].lower().split('d')); return _print([random.randint(1,m) for _ in range(n)])
 except Exception:return 2
def reverse(a): return _print(' '.join(a)[::-1])
def upper(a): return _print(' '.join(a).upper())
def lower(a): return _print(' '.join(a).lower())
def shuffle(a):
 x=' '.join(a).split(','); random.shuffle(x); return _print(','.join(x))
def pick_number(a):
 try:return _print(random.randint(int(a[0]),int(a[1])))
 except Exception:return 2
def flip_multiple(a): return _print([random.choice(['heads','tails']) for _ in range(int(a[0]))])
COMMANDS={'note-add':note_add,'note-list':note_list,'note-clear':note_clear,'todo-add':todo_add,'todo-list':todo_list,'todo-done':todo_done,'todo-clear':todo_clear,'calc':calc,'timer':timer,'stopwatch':stopwatch,'pomodoro':pomodoro,'word-count':word_count,'char-count':char_count,'quote':quote,'coin':coin,'dice':dice,'random-pick':random_pick,'password':password,'uuid':uid,'base64-encode':b64e,'base64-decode':b64d,'ascii-banner':banner,'countdown-days':countdown,'age':age,'color':color,'motivate':motivate,'roll':roll,'reverse-text':reverse,'upper':upper,'lower':lower,'shuffle':shuffle,'pick-number':pick_number,'flip-multiple':flip_multiple}
