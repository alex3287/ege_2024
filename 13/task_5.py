# Сеть задана
# IP-адресом 117.32.0.0 и маской сети 255.224.0.0. Сколько в этой сети IP-адресов,
# которые имеют ровно два одинаковых по значению байта? IP-адрес сети и
# широковещательный адрес учитывать не следует
from ipaddress import *


network = ip_network('117.32.0.0/255.224.0.0')
count = 0
for ip in network:
    ip_s = str(ip)
    A = [int(i) for i in ip_s.split('.')] # 123.33.13.3
    print(ip, A, set(A))
    if len(set(A)) == 3:
        # print(ip, A, set(A))
        count += 1
print(count)


# 40640

