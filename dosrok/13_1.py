from ipaddress import *


network = ip_network('105.224.200.224/255.255.255.224')
print(network)
count = 0
for ip in network:
    temp = bin(int(ip))[2:]
    if temp.count('1')%4 == 0:
        count += 1
print(count)