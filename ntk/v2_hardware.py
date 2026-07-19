"""Hardware information tools."""
import os,platform,shutil
from . import util

def _ps():
 try: import psutil; return psutil
 except ImportError: return None
def _out(x): print(x); return 0
def cpu(a): return _out(platform.processor())
def cpu_cores(a): return _out(os.cpu_count())
def cpu_freq(a):
 p=_ps(); return _out(p.cpu_freq() if p else 'unknown')
def gpu(a): return _out('nvidia-smi/lspci lookup')
def ram(a): return total_ram(a)
def disks(a): return _out(__import__('shutil').disk_usage('/'))
def motherboard(a): return _out('unknown')
def bios(a): return _out('unknown')
def macs(a): return _out('network interfaces')
def adapters(a): return _out('network interfaces')
def battery(a):
 p=_ps(); return _out(p.sensors_battery() if p else 'unknown')
def temps(a):
 p=_ps(); return _out(p.sensors_temperatures() if p else 'unknown')
def usage(a):
 p=_ps(); return _out(p.cpu_percent() if p else 'unknown')
def total_ram(a):
 p=_ps(); return _out(p.virtual_memory().total if p else 'unknown')
def free_ram(a):
 p=_ps(); return _out(p.virtual_memory().available if p else 'unknown')
def disk_count(a): return _out(len(__import__('glob').glob('/dev/sd?')))
def partition_count(a):
 p=_ps(); return _out(len(p.disk_partitions()) if p else 'unknown')
def virtualization(a): return _out('unknown')
def vendor(a): return _out(platform.processor())
def model(a): return _out(platform.machine())
def architecture(a): return _out(platform.architecture())
def byte_order(a): return _out(__import__('sys').byteorder)
def logical(a): return _out(os.cpu_count())
def physical(a):
 p=_ps(); return _out(p.cpu_count(logical=False) if p else 'unknown')
def swap(a):
 p=_ps(); return _out(p.swap_memory() if p else 'unknown')
def boot_device(a): return _out('unknown')
def usb(a): return _out('lsusb lookup')
def monitor(a): return _out('display lookup')
def ram_usage(a):
 p=_ps(); return _out(p.virtual_memory().percent if p else 'unknown')
def disk_model(a): return _out('udev lookup')
def load(a): return _out(os.getloadavg() if hasattr(os,'getloadavg') else 'unknown')
def core_temps(a): return temps(a)
COMMANDS={'cpu':cpu,'cpu-cores':cpu_cores,'cpu-freq':cpu_freq,'gpu':gpu,'ram':ram,'disks':disks,'motherboard':motherboard,'bios':bios,'mac-addresses':macs,'network-adapters':adapters,'battery':battery,'sensors-temp':temps,'cpu-usage':usage,'total-ram':total_ram,'free-ram':free_ram,'disk-count':disk_count,'partition-count':partition_count,'virtualization':virtualization,'cpu-vendor':vendor,'cpu-model':model,'architecture':architecture,'byte-order':byte_order,'logical-cores':logical,'physical-cores':physical,'swap-total':swap,'boot-device-hint':boot_device,'usb-hint':usb,'monitor-hint':monitor,'ram-usage':ram_usage,'disk-model-hint':disk_model,'load-avg':load,'core-temps':core_temps}
