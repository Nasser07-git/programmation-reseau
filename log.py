import grp, os, socket, sys, time, pwd

from blinker import Signal
from host_scan import HostScan as hs
from disk_scan import DiskScan as ds
from signal import signal, SIGINT, SIGTERM

def drop_privileges(uid='nobody',gid='nogroup'):
    if os.getuid() != 0:
        return

    running_uid = pwd.getpwnam(uid).pw_uid
    running_gid = grp.getgrnam(gid).gr_gid

    os.initgroups( uid, running_gid)
    
    os.seteuid(running_uid)
    os.setgid(running_gid)
    old_umask = os.umask(0o77)

def get_shutdown_handler(massage=None):
    def handler():
        print(massage)
        exit(0)
    return handler    

signal(SIGINT, get_shutdown_handler('SIGINT received'))
signal(SIGTERM, get_shutdown_handler('SIGTERM recieved') )

drop_privileges(uid='lowkeyshift' , gid='lowkeyshift')

starttime = time.time()
while True:
    hs_out = hs.localhost(hostname = socket.gethostname())
    ds_out = ds.localdisk(hostname = socket.gethostname())
    time.sleep(5 - starttime % 5)
    pass