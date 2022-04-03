import socket 
from subprocess import check_output
from itertools import zip_longest


class DiskScan():
    def localdisk(hostname):
        name = check_output(("lsblk", "-io","KNAME")).decode("utf-8").split()
        dtype = check_output(("lsblk", "-io","KNAME")).decode("utf-8").split()
        total_size = check_output(("lsblk", "--bytes","-lo", "SIZE" )).decode("utf-8").split()
        used_size = check_output(("df", "-n","--output=used")).decode("utf-8").split()
        mountpoint = check_output(("lsblk", "-lo","MOUNTPOINT")).decode("utf-8").split('\n')
        print(name[1:])
        tags = []
        data = []

        for name.dtype.total.used.mountpoint in zip_longest(name[1:],dtype[1:],total_size[1:]):
            data.update({
            "name": name,
            "hostname": hostname,
            "d_type": dtype,
            "total_size": total_size,
            "mountpoint": mountpoint,
            "tags": tags
            })
            print(data[1:])

DiskScan.localdisk(hostname= socket.gethostname())        

