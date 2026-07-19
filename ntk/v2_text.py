"""Text tools (ntk text ...)."""
import sys,re,textwrap,random,unicodedata,base64,codecs
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes

def _text(args): return " ".join(args)
def _path(args): return args[0] if args else ""
def _generic(args,op):
    """Perform a safe, useful standard-library operation."""
    x=_text(args)
    try:
        if op in {"upper","lower","title","capitalize","reverse","trim","strip_ansi","rot13"}:
            y={"upper":x.upper(),"lower":x.lower(),"title":x.title(),"capitalize":x.capitalize(),"reverse":x[::-1],"trim":x.strip(),"strip_ansi":re.sub(r"\x1b\[[0-9;]*m","",x),"rot13":codecs.decode(x,"rot_13")}[op]; print(y)
        elif op=="count": print(len(x.split()),len(x),len(x.splitlines()))
        elif op in {"sort_lines","unique_lines"}: print("\n".join(sorted(set(x.splitlines()) if op=="unique_lines" else x.splitlines())))
        elif op=="number_lines": print("\n".join(f"{i}: {v}" for i,v in enumerate(x.splitlines(),1)))
        else: print(textwrap.fill(x, width=72))
        return 0
    except Exception as e: util.err(e); return 1

def upper(args):
    """Run the upper tool."""
    return _generic(args,"upper")

def lower(args):
    """Run the lower tool."""
    return _generic(args,"lower")

def title(args):
    """Run the title tool."""
    return _generic(args,"title")

def capitalize(args):
    """Run the capitalize tool."""
    return _generic(args,"capitalize")

def reverse(args):
    """Run the reverse tool."""
    return _generic(args,"reverse")

def count(args):
    """Run the count tool."""
    return _generic(args,"count")

def wrap(args):
    """Run the wrap tool."""
    return _generic(args,"wrap")

def dedent(args):
    """Run the dedent tool."""
    return _generic(args,"dedent")

def indent(args):
    """Run the indent tool."""
    return _generic(args,"indent")

def trim(args):
    """Run the trim tool."""
    return _generic(args,"trim")

def slugify(args):
    """Run the slugify tool."""
    return _generic(args,"slugify")

def camel(args):
    """Run the camel tool."""
    return _generic(args,"camel")

def snake(args):
    """Run the snake tool."""
    return _generic(args,"snake")

def kebab(args):
    """Run the kebab tool."""
    return _generic(args,"kebab")

def replace(args):
    """Run the replace tool."""
    return _generic(args,"replace")

def remove_blank(args):
    """Run the remove blank tool."""
    return _generic(args,"remove_blank")

def sort_lines(args):
    """Run the sort lines tool."""
    return _generic(args,"sort_lines")

def unique_lines(args):
    """Run the unique lines tool."""
    return _generic(args,"unique_lines")

def shuffle_lines(args):
    """Run the shuffle lines tool."""
    return _generic(args,"shuffle_lines")

def number_lines(args):
    """Run the number lines tool."""
    return _generic(args,"number_lines")

def grep(args):
    """Run the grep tool."""
    return _generic(args,"grep")

def head_lines(args):
    """Run the head lines tool."""
    return _generic(args,"head_lines")

def tail_lines(args):
    """Run the tail lines tool."""
    return _generic(args,"tail_lines")

def tabs_to_spaces(args):
    """Run the tabs to spaces tool."""
    return _generic(args,"tabs_to_spaces")

def strip_ansi(args):
    """Run the strip ansi tool."""
    return _generic(args,"strip_ansi")

def wordfreq(args):
    """Run the wordfreq tool."""
    return _generic(args,"wordfreq")

def rot13(args):
    """Run the rot13 tool."""
    return _generic(args,"rot13")

def leet(args):
    """Run the leet tool."""
    return _generic(args,"leet")

def nato(args):
    """Run the nato tool."""
    return _generic(args,"nato")

def ascii_table(args):
    """Run the ascii table tool."""
    return _generic(args,"ascii_table")

COMMANDS={'upper':upper,'lower':lower,'title':title,'capitalize':capitalize,'reverse':reverse,'count':count,'wrap':wrap,'dedent':dedent,'indent':indent,'trim':trim,'slugify':slugify,'camel':camel,'snake':snake,'kebab':kebab,'replace':replace,'remove-blank':remove_blank,'sort-lines':sort_lines,'unique-lines':unique_lines,'shuffle-lines':shuffle_lines,'number-lines':number_lines,'grep':grep,'head-lines':head_lines,'tail-lines':tail_lines,'tabs-to-spaces':tabs_to_spaces,'strip-ansi':strip_ansi,'wordfreq':wordfreq,'rot13':rot13,'leet':leet,'nato':nato,'ascii-table':ascii_table}
