#demo 2024
from ipaddress import *


network = ip_network('192.168.32.160/255.255.255.240')
# print(network)
# ip = ip_address('192.168.32.160')
# print(ip)
# print(int(ip))
# print(f'{int(ip):b}')
for ip in network:
    ip_s = f'{int(ip):b}'
    print(ip_s.count('1'), sum(list(map(int, ip_s))))

