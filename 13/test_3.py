# Сеть задана
# IP-адресом 117.32.0.0 и маской сети 255.224.0.0. Сколько в этой сети IP-адресов,
# которые имеют ровно два одинаковых по значению байта? IP-адрес сети и
# широковещательный адрес учитывать не следует
from ipaddress import *


network = ip_network('117.32.0.0/255.224.0.0')
count = 0
for ip in network:
    ip_s = str(ip)
    A = [int(i) for i in ip_s.split('.')]
    suma = A.count(A[0]) + A.count(A[1]) + A.count(A[2]) + A.count(A[3])
    if suma == 6:
        count += 1
print(count)

