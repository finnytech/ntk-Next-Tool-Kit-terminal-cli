"""Web tools (ntk web ...)."""
import os,sys,time,json,re,urllib.parse,urllib.request
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        u=_path(args)
        if op in {"url_encode","url_decode","query_parse"}: print(urllib.parse.quote(u) if op=="url_encode" else urllib.parse.unquote(u))
        else:
            r=urllib.request.urlopen(u or "https://example.com",timeout=10); print(r.status); print(r.read(4096).decode("utf8","replace"))
        return 0
    except Exception as e: util.err(e); return 1

def get(args):
    """Run the get tool."""
    return _generic(args,"get")

def post(args):
    """Run the post tool."""
    return _generic(args,"post")

def head(args):
    """Run the head tool."""
    return _generic(args,"head")

def status(args):
    """Run the status tool."""
    return _generic(args,"status")

def headers(args):
    """Run the headers tool."""
    return _generic(args,"headers")

def download(args):
    """Run the download tool."""
    return _generic(args,"download")

def title(args):
    """Run the title tool."""
    return _generic(args,"title")

def links(args):
    """Run the links tool."""
    return _generic(args,"links")

def meta_tags(args):
    """Run the meta tags tool."""
    return _generic(args,"meta_tags")

def redirects(args):
    """Run the redirects tool."""
    return _generic(args,"redirects")

def response_time(args):
    """Run the response time tool."""
    return _generic(args,"response_time")

def bench(args):
    """Run the bench tool."""
    return _generic(args,"bench")

def user_agent_test(args):
    """Run the user agent test tool."""
    return _generic(args,"user_agent_test")

def robots(args):
    """Run the robots tool."""
    return _generic(args,"robots")

def sitemap(args):
    """Run the sitemap tool."""
    return _generic(args,"sitemap")

def favicon_url(args):
    """Run the favicon url tool."""
    return _generic(args,"favicon_url")

def http2_check(args):
    """Run the http2 check tool."""
    return _generic(args,"http2_check")

def gzip_check(args):
    """Run the gzip check tool."""
    return _generic(args,"gzip_check")

def content_type(args):
    """Run the content type tool."""
    return _generic(args,"content_type")

def ip_of_host(args):
    """Run the ip of host tool."""
    return _generic(args,"ip_of_host")

def cookies_show(args):
    """Run the cookies show tool."""
    return _generic(args,"cookies_show")

def cors_check(args):
    """Run the cors check tool."""
    return _generic(args,"cors_check")

def cache_headers(args):
    """Run the cache headers tool."""
    return _generic(args,"cache_headers")

def security_headers(args):
    """Run the security headers tool."""
    return _generic(args,"security_headers")

def api_get_json(args):
    """Run the api get json tool."""
    return _generic(args,"api_get_json")

def json_endpoint_keys(args):
    """Run the json endpoint keys tool."""
    return _generic(args,"json_endpoint_keys")

def url_encode(args):
    """Run the url encode tool."""
    return _generic(args,"url_encode")

def url_decode(args):
    """Run the url decode tool."""
    return _generic(args,"url_decode")

def query_parse(args):
    """Run the query parse tool."""
    return _generic(args,"query_parse")

def ssl_expiry_days(args):
    """Run the ssl expiry days tool."""
    return _generic(args,"ssl_expiry_days")

def ping_http(args):
    """Run the ping http tool."""
    return _generic(args,"ping_http")

COMMANDS={'get':get,'post':post,'head':head,'status':status,'headers':headers,'download':download,'title':title,'links':links,'meta-tags':meta_tags,'redirects':redirects,'response-time':response_time,'bench':bench,'user-agent-test':user_agent_test,'robots':robots,'sitemap':sitemap,'favicon-url':favicon_url,'http2-check':http2_check,'gzip-check':gzip_check,'content-type':content_type,'ip-of-host':ip_of_host,'cookies-show':cookies_show,'cors-check':cors_check,'cache-headers':cache_headers,'security-headers':security_headers,'api-get-json':api_get_json,'json-endpoint-keys':json_endpoint_keys,'url-encode':url_encode,'url-decode':url_decode,'query-parse':query_parse,'ssl-expiry-days':ssl_expiry_days,'ping-http':ping_http}
