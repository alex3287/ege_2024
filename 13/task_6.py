# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в этой сети.
# Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла
# и маске сети. Сеть задана IP-адресом 202.75.38.160 и маской сети 255.255.255.240.
# Сколько в этой сети IP-адресов, у которых в двоичной записи IP-адреса имеется сочетание
# трех подряд идущих единиц? В ответе укажите только число.

from ipaddress import *


network = ip_network('202.75.38.160/255.255.255.240')
for ip in network:
    print(f'{int(ip):b}'.count('111'))


#111111110101111001011

