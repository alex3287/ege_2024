# Сеть задана IP-адресом 255.211.33.160 и маской сети 255.255.А.0, где А —
# некоторое допустимое для записи маски число. Определите минимальное
# значение А, для которого для всех IP-адресов этой сети в двоичной записи
# IP-адреса суммарное количество единиц в левых двух байтах не менее
# суммарного количества единиц в правых двух байтах.
# В ответе укажите только число
from ipaddress import *


# 0 128 192 224 240 248 252 254 255

network = ip_network(f'255.211.33.160/255.255.{240}.0', False)
for ip in network:
    ip_s = str(ip)
    b1, b2, b3, b4 = ip_s.split('.')
    left = f'{int(b1):b}'.count('1') + f'{int(b2):b}'.count('1')
    right = f'{int(b3):b}'.count('1') + f'{int(b4):b}'.count('1')
    if left < right:
        print('No')
        break
else:
    print('Yes')

