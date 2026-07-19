"""Network tools (ntk net ...)."""
import os, re, socket, ssl, struct, subprocess, time, urllib.parse, urllib.request, ipaddress, json
from . import util
from .util import col, C, run, IS_WINDOWS

def _arg(args, usage):
    if not args: util.err("usage: " + usage); return None
    return args[0]

def ip(args):
    """Show local and public IP addresses."""
    host=socket.gethostname(); local=[]
    try: local=sorted({x[4][0] for x in socket.getaddrinfo(host,None)})
    except OSError: pass
    public="unavailable"
    try: public=urllib.request.urlopen("https://api.ipify.org",timeout=5).read().decode().strip()
    except Exception: pass
    util.header("IP addresses"); util.kv("Hostname",host); util.kv("Local",", ".join(local)); util.kv("Public",public); return 0

def ping(args):
    host=_arg(args,"ntk net ping <host> [count]")
    if not host:return 2
    n=args[1] if len(args)>1 else "4"; cmd=["ping","-n" if IS_WINDOWS else "-c",n,host]; rc,out,e=run(cmd,timeout=30); print(out or e); return rc

def ports(args):
    host=_arg(args,"ntk net ports <host> [port|start-end]")
    if not host:return 2
    spec=args[1] if len(args)>1 else "1-1024"; ports=[]
    try:
        if "-" in spec:
            a,b=map(int,spec.split("-",1)); ports=list(range(a,b+1))
        else: ports=[int(x) for x in spec.split(",")]
    except ValueError: util.err("invalid port specification"); return 2
    rows=[]
    for p in ports[:10000]:
        s=socket.socket(); s.settimeout(.25)
        try: rc=s.connect_ex((host,p));
        except OSError: rc=1
        finally:s.close()
        if rc==0: rows.append((p,"open"))
    util.table(rows,headers=["Port","State"]); return 0

def dns(args):
    name=_arg(args,"ntk net dns <name>");
    if not name:return 2
    try: rows=sorted({(x[4][0],) for x in socket.getaddrinfo(name,None)})
    except OSError as e: util.err(str(e)); return 1
    util.table(rows,headers=["Address"]); return 0

def whois(args):
    name=_arg(args,"ntk net whois <domain>");
    if not name:return 2
    cmd="whois" if util.which("whois") else ("powershell" if IS_WINDOWS else None)
    if not cmd: util.warn("whois command not available"); return 1
    c=[cmd,"-NoProfile","-Command",f"whois {name}"] if IS_WINDOWS else [cmd,name]; rc,out,e=run(c,timeout=20); print(out or e); return rc

def speedtest(args):
    """Measure download speed from a public endpoint."""
    url=args[0] if args else "https://speed.hetzner.de/100MB.bin"; start=time.time()
    try:
        r=urllib.request.urlopen(url,timeout=15); total=0
        while total<10*1024*1024:
            b=r.read(65536)
            if not b:break
            total+=len(b)
        elapsed=max(time.time()-start,.001); util.kv("Downloaded",util.human_bytes(total)); util.kv("Speed",f"{total/elapsed/1024/1024:.2f} MiB/s"); return 0
    except Exception as e: util.err(str(e)); return 1

def _http(args, method):
    url=_arg(args,f"ntk net http-{method.lower()} <url> [data]");
    if not url:return 2
    data=(args[1].encode() if len(args)>1 else None); req=urllib.request.Request(url,data=data,method=method)
    try:
        with urllib.request.urlopen(req,timeout=20) as r: print(r.read().decode(errors="replace")); return 0
    except Exception as e: util.err(str(e)); return 1

def http_get(args): return _http(args,"GET")
def http_post(args): return _http(args,"POST")
def headers(args):
    url=_arg(args,"ntk net headers <url>");
    if not url:return 2
    try:
        with urllib.request.urlopen(urllib.request.Request(url,method="HEAD"),timeout=15) as r:
            util.table([(k,v) for k,v in r.headers.items()],headers=["Header","Value"])
        return 0
    except Exception as e: util.err(str(e)); return 1

def traceroute(args):
    host=_arg(args,"ntk net traceroute <host>");
    if not host:return 2
    cmd=["tracert" if IS_WINDOWS else "traceroute",host]; rc,out,e=run(cmd,timeout=60); print(out or e); return rc

def interfaces(args):
    cmd=["ipconfig","/all"] if IS_WINDOWS else ["ip","addr"]; rc,out,e=run(cmd); print(out or e); return rc

def wifi_list(args):
    cmd=["netsh","wlan","show","networks","mode=bssid"] if IS_WINDOWS else ["nmcli","-f","SSID,SIGNAL,SECURITY","dev","wifi"]; rc,out,e=run(cmd); print(out or e); return rc

def wifi_pass(args):
    name=_arg(args,"ntk net wifi-pass <ssid>");
    if not name:return 2
    if not IS_WINDOWS: util.warn("wifi-pass is supported through netsh on Windows"); return 1
    rc,out,e=run(["netsh","wlan","show","profile",f"name={name}","key=clear"]); print(out or e); return rc

def subnet(args):
    s=_arg(args,"ntk net subnet <network>");
    if not s:return 2
    try:
        n=ipaddress.ip_network(s,strict=False); util.kv("Network",n); util.kv("Netmask",n.netmask); util.kv("Hosts",n.num_addresses-2 if n.num_addresses>2 else max(0,n.num_addresses)); util.kv("Broadcast",getattr(n,"broadcast_address","")); return 0
    except ValueError as e: util.err(str(e)); return 2

def ssh_test(args):
    host=_arg(args,"ntk net ssh-test <host> [port]");
    if not host:return 2
    port=int(args[1]) if len(args)>1 else 22; s=socket.create_connection((host,port),3); banner=s.recv(256).decode(errors="replace"); s.close(); util.ok(f"{host}:{port} reachable"); print(banner.strip()); return 0

def ssl_tool(args):
    host=_arg(args,"ntk net ssl <host> [port]");
    if not host:return 2
    port=int(args[1]) if len(args)>1 else 443
    try:
        with socket.create_connection((host,port),5) as s, ssl.create_default_context().wrap_socket(s,server_hostname=host) as t:
            c=t.getpeercert(); util.kv("Subject",c.get("subject")); util.kv("Issuer",c.get("issuer")); util.kv("Expires",c.get("notAfter")); util.kv("Cipher",t.cipher()); return 0
    except Exception as e: util.err(str(e)); return 1

def mac(args):
    cmd=["getmac"] if IS_WINDOWS else ["ip","link"]; rc,out,e=run(cmd); print(out or e); return rc

def _lookup(args, typ):
    name=_arg(args,f"ntk net {typ} <domain>");
    if not name:return 2
    if util.which("nslookup"):
        rc,out,e=run(["nslookup",f"-type={typ}",name]); print(out or e); return rc
    util.warn("nslookup unavailable"); return 1

def cname(args): return _lookup(args,"cname")
def mx(args): return _lookup(args,"mx")
def bgp(args): return _lookup(args,"txt")
def netstat(args):
    rc,out,e=run(["netstat","-ano"] if IS_WINDOWS else ["ss","-tulnp"]); print(out or e); return rc

def wakeonlan(args):
    macaddr=_arg(args,"ntk net wakeonlan <mac> [broadcast]");
    if not macaddr:return 2
    raw=bytes.fromhex(re.sub("[^0-9a-fA-F]","",macaddr));
    if len(raw)!=6: util.err("invalid MAC address"); return 2
    packet=b"\xff"*6+raw*16; b=args[1] if len(args)>1 else "255.255.255.255"; s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1); s.sendto(packet,(b,9)); s.close(); util.ok("magic packet sent"); return 0

def http_status(args):
    codes={200:"OK",201:"Created",204:"No Content",301:"Moved Permanently",302:"Found",304:"Not Modified",400:"Bad Request",401:"Unauthorized",403:"Forbidden",404:"Not Found",418:"I'm a teapot",429:"Too Many Requests",500:"Internal Server Error",502:"Bad Gateway",503:"Service Unavailable"}
    util.table(sorted(codes.items()),headers=["Code","Meaning"]); return 0

def url_parser(args):
    u=_arg(args,"ntk net url-parser <url>");
    if not u:return 2
    p=urllib.parse.urlparse(u); util.table([(k,getattr(p,k)) for k in ("scheme","netloc","path","params","query","fragment")],headers=["Part","Value"]); return 0

def cert_gen(args):
    out=args[0] if args else "cert.pem"
    if not util.which("openssl"): util.warn("openssl not found"); return 1
    rc,o,e=run(["openssl","req","-x509","-newkey","rsa:2048","-keyout",out+".key","-out",out,"-days","365","-nodes","-subj","/CN=localhost"],timeout=30); print(o or e); return rc

def speed_ping(args):
    host=_arg(args,"ntk net speed-ping <host> [count]");
    if not host:return 2
    n=int(args[1]) if len(args)>1 else 4; vals=[]
    for _ in range(n):
        t=time.perf_counter()
        try: socket.gethostbyname(host); vals.append((time.perf_counter()-t)*1000)
        except OSError: pass
    if vals: util.kv("Min/avg/max",f"{min(vals):.1f}/{sum(vals)/len(vals):.1f}/{max(vals):.1f} ms")
    return 0 if vals else 1

COMMANDS={"ip":ip,"ping":ping,"ports":ports,"dns":dns,"whois":whois,"speedtest":speedtest,"http-get":http_get,"http-post":http_post,"headers":headers,"traceroute":traceroute,"interfaces":interfaces,"wifi-list":wifi_list,"wifi-pass":wifi_pass,"subnet":subnet,"ssh-test":ssh_test,"ssl":ssl_tool,"mac":mac,"cname":cname,"mx":mx,"bgp":bgp,"netstat":netstat,"wakeonlan":wakeonlan,"http-status":http_status,"url-parser":url_parser,"cert-gen":cert_gen,"speed-ping":speed_ping}
