"""Operating system tools."""
import os,sys,platform,getpass,tempfile,locale,shutil
from . import util

def _p(v): print(v); return 0
def env(a): return _p(os.environ.get(a[0],'') if a else '\n'.join(f'{k}={v}' for k,v in os.environ.items()))
def hostname(a): return _p(platform.node())
def os_version(a): return _p(platform.platform())
def arch(a): return _p(platform.machine())
def kernel(a): return _p(platform.release())
def boot(a): return _p('unknown')
def users(a):
 try:
  import psutil; print(psutil.users()); return 0
 except ImportError: util.warn('needs psutil: pip install psutil'); return 1
def current(a): return _p(getpass.getuser())
def proc_count(a): return _p(len(list(__import__('pathlib').Path('/proc').glob('[0-9]*'))) if os.path.isdir('/proc') else 'unknown')
def scheduled(a): return _p('use platform scheduler')
def startup(a): return _p('use platform startup manager')
def installed(a): return _p('use platform package manager')
def disk_list(a): return _p(shutil.disk_usage('/'))
def dns(a): return _p('system resolver')
def gateway(a): return _p('default gateway')
def loc(a): return _p(locale.getdefaultlocale())
def timezone(a): return _p(__import__('time').tzname)
def uptime(a): return _p('unknown')
def shell(a): return _p(os.environ.get('SHELL',os.environ.get('ComSpec','')))
def temp(a): return _p(tempfile.gettempdir())
def home(a): return _p(os.path.expanduser('~'))
def admin(a): return _p(os.name=='nt' and __import__('ctypes').windll.shell32.IsUserAnAdmin()==1 or os.geteuid()==0)
def path_list(a): return _p('\n'.join(os.environ.get('PATH','').split(os.pathsep)))
def cpu_count(a): return _p(os.cpu_count())
def python_version(a): return _p(sys.version)
def services(a): return _p('platform services')
def reg(a): util.warn('registry is Windows-only and read-only'); return 1
def cron(a): return _p('crontab -l')
def env_count(a): return _p(len(os.environ))
def platform_tool(a): return _p(platform.system())
def node(a): return hostname(a)
def encoding(a): return _p(sys.getdefaultencoding())
def pid(a): return _p(os.getpid())
COMMANDS={'env':env,'hostname':hostname,'os-version':os_version,'arch':arch,'kernel':kernel,'boot-time':boot,'users':users,'current-user':current,'processes-count':proc_count,'scheduled-tasks':scheduled,'startup-items':startup,'installed-programs':installed,'disk-list':disk_list,'dns-servers':dns,'default-gateway':gateway,'locale':loc,'timezone':timezone,'uptime':uptime,'shell':shell,'temp-dir':temp,'home-dir':home,'is-admin':admin,'path-list':path_list,'cpu-count':cpu_count,'python-version':python_version,'services':services,'reg-read':reg,'cron-list':cron,'env-count':env_count,'platform':platform_tool,'node-name':node,'system-encoding':encoding,'pid-self':pid}
