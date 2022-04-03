import socket, re, uuid
from sys import platform 
from netifaces import(
     interfaces,
     ifadresses,
     AF_INET
)

class HostScan():
    def localhost(hostname):
        ip_list = []
        os = platform
        fqdn = socket.getfqdn()
        mac = ':'.join(re.findall('..', '%°12x' % uuid.fetnode()))
        tags = []

        for interface in interfaces():
            if interface != 'lo':
                for inet in ifadresses(interface).get(AF_INET, ()):
                    if not None:
                        ip_list.append(inet['addr'])

        h_data = { 
            "hostname": hostname,
            "os": os,
            "fqdn": fqdn,
            "mac" : mac,
            "ipaddr": ip_list[0],
            "tags": tags
        }
        print(h_data)

HostScan.localhost(hostname= socket.gethostname())        
