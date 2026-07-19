"""Network tools (ntk network ...)."""
import os,sys,socket,urllib.parse,urllib.request,ssl,ipaddress,time
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes
def _arg(a): return a[0] if a else ''
def _net(a,op):
    h=_arg(a)
    try:
        if op=='ping': return run(['ping','-n' if IS_WINDOWS else '-c','1',h],timeout=8)[0]
        if op in ('dns-lookup','mx','txt','ns'): util.table([(x[0],x[4][0]) for x in socket.getaddrinfo(h,None)],headers=['Family','Address'])
        elif op=='reverse-dns': util.kv('Name',socket.gethostbyaddr(h)[0])
        elif op=='whois': return run(['whois',h],timeout=10)[0] if which('whois') else (util.warn('needs whois') or 1)
        elif op=='ports-scan': util.table([(p,'open' if socket.create_connection((h,p),.3) else 'closed') for p in [22,53,80,443]],headers=['Port','State'])
        elif op=='local-ip': s=socket.socket(); s.connect(('8.8.8.8',80)); print(s.getsockname()[0]); s.close()
        elif op=='interfaces': return run(['ip','addr'] if not IS_WINDOWS else ['ipconfig'])[0]
        elif op=='mac': return run(['ip','link'] if not IS_WINDOWS else ['getmac'])[0]
        elif op=='gateway': return run(['ip','route'] if not IS_WINDOWS else ['route','print'])[0]
        elif op in ('http-get','my-ip','is-online'): print(urllib.request.urlopen(h or 'https://api.ipify.org',timeout=10).read().decode('utf8','replace'))
        elif op=='http-status': util.kv('Status',urllib.request.urlopen(h,timeout=10).status)
        elif op=='headers': print(urllib.request.urlopen(h,timeout=10).headers)
        elif op in ('ssl-info','cert-expiry'): c=ssl.create_default_context().wrap_socket(socket.socket(),server_hostname=h); c.settimeout(5); c.connect((h,443)); print(c.getpeercert()); c.close()
        elif op=='subnet-calc': n=ipaddress.ip_network(h,strict=False); util.table([('network',n.network_address),('broadcast',n.broadcast_address),('hosts',n.num_addresses)])
        elif op=='url-parse': util.table([(k,getattr(urllib.parse.urlparse(h),k)) for k in ('scheme','netloc','path','query')])
        elif op in ('traceroute','wifi-list','netstat','arp'): return run([{'traceroute':'traceroute','wifi-list':'nmcli','netstat':'netstat','arp':'arp'}[op]],timeout=15)[0]
        elif op=='download': urllib.request.urlretrieve(h,a[1] if len(a)>1 else 'download'); util.ok('downloaded')
        elif op=='speed-ping': t=time.time(); [_net(a,'ping') for _ in range(3)]; util.kv('Elapsed',time.time()-t)
        elif op in ('host-up','ip-geo','dns-cache'): return _net(a,'ping' if op=='host-up' else 'http-get')
        return 0
    except Exception as e: util.err(e); return 1

def make(name,desc):
    def f(args):
        """%s""" % desc
        return _net(args,name)
    f.__name__=name.replace('-','_'); return f
_names=['ping','dns-lookup','reverse-dns','mx','txt','ns','whois','ports-scan','my-ip','local-ip','interfaces','mac','gateway','http-get','http-post','http-status','headers','ssl-info','cert-expiry','subnet-calc','url-parse','traceroute','wifi-list','netstat','is-online','download','speed-ping','host-up','arp','ip-geo','dns-cache']
COMMANDS={n:make(n,n.replace('-',' ')+' network tool') for n in _names}
