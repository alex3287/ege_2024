from ipaddress import *


network = ip_network('192.168.32.160/255.255.255.240')
# print(network) # SIDR натация
for ip in network:
    print(bin(int(ip)).count('1'))

# ip = ip_address('1.8.2.160')
# ip2 = '1.8.2.160'
# print(ip, ip2)
# print(bin(int(ip))[2:])
# # 1 => 00000001