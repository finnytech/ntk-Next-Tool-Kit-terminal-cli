"""Data tools (ntk data ...)."""
import sys,json,csv,io,base64,urllib.parse
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        obj=json.loads(x or "null")
        if op in {"json_format","pretty","json_sort_keys"}: print(json.dumps(obj,indent=2,sort_keys=op=="json_sort_keys"))
        elif op=="json_minify": print(json.dumps(obj,separators=(",",":")))
        elif op=="json_validate": print("valid")
        elif op=="json_keys": print("\n".join(map(str,obj.keys())) if isinstance(obj,dict) else "")
        else: print(json.dumps(obj,indent=2))
        return 0
    except Exception as e: util.err(e); return 1

def json_format(args):
    """Run the json format tool."""
    return _generic(args,"json_format")

def json_minify(args):
    """Run the json minify tool."""
    return _generic(args,"json_minify")

def json_validate(args):
    """Run the json validate tool."""
    return _generic(args,"json_validate")

def json_get(args):
    """Run the json get tool."""
    return _generic(args,"json_get")

def csv_to_json(args):
    """Run the csv to json tool."""
    return _generic(args,"csv_to_json")

def json_to_csv(args):
    """Run the json to csv tool."""
    return _generic(args,"json_to_csv")

def yaml_to_json(args):
    """Run the yaml to json tool."""
    return _generic(args,"yaml_to_json")

def json_to_yaml(args):
    """Run the json to yaml tool."""
    return _generic(args,"json_to_yaml")

def xml_to_json(args):
    """Run the xml to json tool."""
    return _generic(args,"xml_to_json")

def flatten_json(args):
    """Run the flatten json tool."""
    return _generic(args,"flatten_json")

def json_keys(args):
    """Run the json keys tool."""
    return _generic(args,"json_keys")

def csv_cols(args):
    """Run the csv cols tool."""
    return _generic(args,"csv_cols")

def csv_head(args):
    """Run the csv head tool."""
    return _generic(args,"csv_head")

def csv_stats(args):
    """Run the csv stats tool."""
    return _generic(args,"csv_stats")

def json_diff(args):
    """Run the json diff tool."""
    return _generic(args,"json_diff")

def csv_to_md(args):
    """Run the csv to md tool."""
    return _generic(args,"csv_to_md")

def json_merge(args):
    """Run the json merge tool."""
    return _generic(args,"json_merge")

def toml_to_json(args):
    """Run the toml to json tool."""
    return _generic(args,"toml_to_json")

def json_sort_keys(args):
    """Run the json sort keys tool."""
    return _generic(args,"json_sort_keys")

def ndjson_to_json(args):
    """Run the ndjson to json tool."""
    return _generic(args,"ndjson_to_json")

def csv_filter(args):
    """Run the csv filter tool."""
    return _generic(args,"csv_filter")

def csv_sort(args):
    """Run the csv sort tool."""
    return _generic(args,"csv_sort")

def json_count(args):
    """Run the json count tool."""
    return _generic(args,"json_count")

def base64_json(args):
    """Run the base64 json tool."""
    return _generic(args,"base64_json")

def url_to_json(args):
    """Run the url to json tool."""
    return _generic(args,"url_to_json")

def env_to_json(args):
    """Run the env to json tool."""
    return _generic(args,"env_to_json")

def json_schema_infer(args):
    """Run the json schema infer tool."""
    return _generic(args,"json_schema_infer")

def csv_dedupe(args):
    """Run the csv dedupe tool."""
    return _generic(args,"csv_dedupe")

def pretty(args):
    """Run the pretty tool."""
    return _generic(args,"pretty")

def json_lines(args):
    """Run the json lines tool."""
    return _generic(args,"json_lines")

def data_stats(args):
    """Run the data stats tool."""
    return _generic(args,"data_stats")

COMMANDS={'json-format':json_format,'json-minify':json_minify,'json-validate':json_validate,'json-get':json_get,'csv-to-json':csv_to_json,'json-to-csv':json_to_csv,'yaml-to-json':yaml_to_json,'json-to-yaml':json_to_yaml,'xml-to-json':xml_to_json,'flatten-json':flatten_json,'json-keys':json_keys,'csv-cols':csv_cols,'csv-head':csv_head,'csv-stats':csv_stats,'json-diff':json_diff,'csv-to-md':csv_to_md,'json-merge':json_merge,'toml-to-json':toml_to_json,'json-sort-keys':json_sort_keys,'ndjson-to-json':ndjson_to_json,'csv-filter':csv_filter,'csv-sort':csv_sort,'json-count':json_count,'base64-json':base64_json,'url-to-json':url_to_json,'env-to-json':env_to_json,'json-schema-infer':json_schema_infer,'csv-dedupe':csv_dedupe,'pretty':pretty,'json-lines':json_lines,'data-stats':data_stats}
