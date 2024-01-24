from ipaddress import *


network = ip_network('10.8.248.131/255.255.255.240', False)
for ip in network:
    print(ip)