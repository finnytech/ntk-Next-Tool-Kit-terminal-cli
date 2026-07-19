"""Git tools (ntk git ...)."""
import os,sys
from . import util
from .util import col,C,run,which,IS_WINDOWS,human_bytes
_NAMES=['status','log','branches','current-branch','remotes','stash-list','tags','contributors','changed-files','diff-stat','last-commit','ahead-behind','root','is-repo','file-history','blame-summary','clean-preview','unstaged','staged','commit-count','first-commit','largest-files','branch-age','orphan-branches','untracked','ignored','config-list','user-info','remote-url','fetch-dry','gc-preview']
def _git(args,op):
    if not which('git'): util.warn('needs git: install git'); return 1
    cmd=['git']
    mapping={'status':['status','--short'],'log':['log','-n',args[0] if args and args[0].isdigit() else '10','--oneline'],'branches':['branch','-a'],'current-branch':['branch','--show-current'],'remotes':['remote','-v'],'stash-list':['stash','list'],'tags':['tag'],'contributors':['shortlog','-sn'],'changed-files':['diff','--name-only'],'diff-stat':['diff','--stat'],'last-commit':['log','-1','--format=full'],'root':['rev-parse','--show-toplevel'],'is-repo':['rev-parse','--is-inside-work-tree'],'file-history':['log','--oneline','--',args[0] if args else '.'],'blame-summary':['blame','--line-porcelain',args[0] if args else '.'],'clean-preview':['clean','-ndx'],'unstaged':['diff','--name-only'],'staged':['diff','--cached','--name-only'],'commit-count':['rev-list','--count','HEAD'],'first-commit':['rev-list','--max-parents=0','HEAD'],'largest-files':['ls-files'],'config-list':['config','--list'],'user-info':['config','user.name'],'remote-url':['remote','get-url','origin'],'fetch-dry':['fetch','--dry-run'],'gc-preview':['gc','--dry-run']}
    c=mapping.get(op,['status']); rc,o,e=run(cmd+c,timeout=20); print(o or e,end=''); return rc
def make(n):
    def f(args):
        """Run git %s.""" % n
        return _git(args,n)
    return f
COMMANDS={n:make(n) for n in _NAMES}
