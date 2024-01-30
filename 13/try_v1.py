from ipaddress import *


network = ip_network('192.168.32.96/255.255.255.224')
k = 0
for ip in network:
    if f'{int(ip):b}'.count('1') % 2 == 0:
        k += 1
print(k)