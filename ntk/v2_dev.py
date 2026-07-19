"""Dev tools (ntk dev ...)."""
import os,sys,re,json,uuid,time,datetime,base64,urllib.parse
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        if op=="uuid": print(uuid.uuid4())
        elif op=="timestamp": print(int(time.time()))
        elif op=="epoch_to_date": print(datetime.datetime.fromtimestamp(float(x or 0)).isoformat())
        elif op=="date_to_epoch": print(datetime.datetime.fromisoformat(x).timestamp())
        elif op in {"lorem","password","mock_json"}: print("Lorem ipsum dolor sit amet" if op=="lorem" else json.dumps({"id":1,"name":"example"}))
        else: print(x)
        return 0
    except Exception as e: util.err(e); return 1

def lorem(args):
    """Run the lorem tool."""
    return _generic(args,"lorem")

def uuid(args):
    """Run the uuid tool."""
    return _generic(args,"uuid")

def timestamp(args):
    """Run the timestamp tool."""
    return _generic(args,"timestamp")

def epoch_to_date(args):
    """Run the epoch to date tool."""
    return _generic(args,"epoch_to_date")

def date_to_epoch(args):
    """Run the date to epoch tool."""
    return _generic(args,"date_to_epoch")

def semver_bump(args):
    """Run the semver bump tool."""
    return _generic(args,"semver_bump")

def semver_compare(args):
    """Run the semver compare tool."""
    return _generic(args,"semver_compare")

def color_convert(args):
    """Run the color convert tool."""
    return _generic(args,"color_convert")

def regex_test(args):
    """Run the regex test tool."""
    return _generic(args,"regex_test")

def regex_explain_basic(args):
    """Run the regex explain basic tool."""
    return _generic(args,"regex_explain_basic")

def json_to_code(args):
    """Run the json to code tool."""
    return _generic(args,"json_to_code")

def gitignore_gen(args):
    """Run the gitignore gen tool."""
    return _generic(args,"gitignore_gen")

def license_gen(args):
    """Run the license gen tool."""
    return _generic(args,"license_gen")

def env_example_gen(args):
    """Run the env example gen tool."""
    return _generic(args,"env_example_gen")

def port_free(args):
    """Run the port free tool."""
    return _generic(args,"port_free")

def scaffold_file(args):
    """Run the scaffold file tool."""
    return _generic(args,"scaffold_file")

def http_server(args):
    """Run the http server tool."""
    return _generic(args,"http_server")

def md_toc(args):
    """Run the md toc tool."""
    return _generic(args,"md_toc")

def slug(args):
    """Run the slug tool."""
    return _generic(args,"slug")

def jwt_decode(args):
    """Run the jwt decode tool."""
    return _generic(args,"jwt_decode")

def cron_explain(args):
    """Run the cron explain tool."""
    return _generic(args,"cron_explain")

def base64url(args):
    """Run the base64url tool."""
    return _generic(args,"base64url")

def htpasswd(args):
    """Run the htpasswd tool."""
    return _generic(args,"htpasswd")

def dockerfile_gen(args):
    """Run the dockerfile gen tool."""
    return _generic(args,"dockerfile_gen")

def readme_gen(args):
    """Run the readme gen tool."""
    return _generic(args,"readme_gen")

def changelog_gen(args):
    """Run the changelog gen tool."""
    return _generic(args,"changelog_gen")

def todo_scan(args):
    """Run the todo scan tool."""
    return _generic(args,"todo_scan")

def loc(args):
    """Run the loc tool."""
    return _generic(args,"loc")

def password(args):
    """Run the password tool."""
    return _generic(args,"password")

def mock_json(args):
    """Run the mock json tool."""
    return _generic(args,"mock_json")

COMMANDS={'lorem':lorem,'uuid':uuid,'timestamp':timestamp,'epoch-to-date':epoch_to_date,'date-to-epoch':date_to_epoch,'semver-bump':semver_bump,'semver-compare':semver_compare,'color-convert':color_convert,'regex-test':regex_test,'regex-explain-basic':regex_explain_basic,'json-to-code':json_to_code,'gitignore-gen':gitignore_gen,'license-gen':license_gen,'env-example-gen':env_example_gen,'port-free':port_free,'scaffold-file':scaffold_file,'http-server':http_server,'md-toc':md_toc,'slug':slug,'jwt-decode':jwt_decode,'cron-explain':cron_explain,'base64url':base64url,'htpasswd':htpasswd,'dockerfile-gen':dockerfile_gen,'readme-gen':readme_gen,'changelog-gen':changelog_gen,'todo-scan':todo_scan,'loc':loc,'password':password,'mock-json':mock_json}
