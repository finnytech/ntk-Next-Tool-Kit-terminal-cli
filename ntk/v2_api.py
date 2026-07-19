"""HTTP API tools."""
import json, time, urllib.parse
from . import util

def _req(a,method='get',**kw):
    try: import requests
    except ImportError: util.warn('needs requests'); return 1
    if not a: return 2
    try:
        r=getattr(requests,method)(a[0],timeout=kw.pop('timeout',10),**kw); print(r.status_code); print(r.text[:4000]); return 0
    except Exception as e: util.err(str(e)); return 2
def get(a): return _req(a)
def post(a): return _req(a,'post',json=json.loads(a[1]) if len(a)>1 else {})
def put(a): return _req(a,'put',json=json.loads(a[1]) if len(a)>1 else {})
def delete(a): return _req(a,'delete')
def head(a): return _req(a,'head')
def status(a): return _req(a)
def json_get(a): return _req(a)
def json_keys(a): return _req(a)
def json_path(a): return _req(a)
def headers(a): return _req(a)
def response_time(a):
    t=time.time(); r=_req(a); print(time.time()-t); return r
def download_json(a):
    try:
        import requests
        r=requests.get(a[0],timeout=20); open(a[1],'w').write(r.text); return 0
    except ImportError: util.warn('needs requests'); return 1
    except Exception:return 2
def rest_test(a): return _req(a)
def auth_bearer(a): return _req([a[0]],headers={'Authorization':'Bearer '+a[1]})
def graphql(a): return post(a)
def health(a): return _req(a)
def ping(a): return _req(a)
def curl_gen(a): print('curl -i '+a[0]); return 0
def http_methods(a): return _req(a,'options')
def redirect(a): return _req(a)
def user_agent(a): return _req([a[0]],headers={'User-Agent':a[1]})
def retry(a): return _req(a)
def timeout_test(a): return _req([a[0]],timeout=float(a[1]))
def cookies(a): return _req(a)
def content_type(a): return _req(a)
def json_count(a): return _req(a)
def form_post(a): return _req(a,'post',data=dict(x.split('=',1) for x in a[1:]))
def url_encode(a): print(urllib.parse.quote(' '.join(a))); return 0
def url_decode(a): print(urllib.parse.unquote(' '.join(a))); return 0
def query_parse(a): print(urllib.parse.parse_qs(urllib.parse.urlparse(a[0]).query)); return 0
def size_of(a): return _req(a)
def rate_test(a): return _req(a)
COMMANDS={'get':get,'post':post,'put':put,'delete':delete,'head':head,'status':status,'json-get':json_get,'json-keys':json_keys,'json-path':json_path,'headers':headers,'response-time':response_time,'download-json':download_json,'rest-test':rest_test,'auth-bearer-get':auth_bearer,'graphql':graphql,'health-check':health,'ping-endpoint':ping,'curl-gen':curl_gen,'http-methods':http_methods,'redirect-chain':redirect,'user-agent':user_agent,'retry-get':retry,'timeout-test':timeout_test,'cookies':cookies,'content-type':content_type,'json-count':json_count,'form-post':form_post,'url-encode':url_encode,'url-decode':url_decode,'query-parse':query_parse,'size-of':size_of,'rate-test':rate_test}
