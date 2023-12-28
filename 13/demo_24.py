from ipaddress import *


network = ip_network('192.168.32.160/255.255.255.240')
for ip in network:
    print(bin(int(ip))[2:].count('1'))

