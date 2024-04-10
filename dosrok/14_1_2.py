from string import *


ABC = '0123456789abcdefghijklmnopq'
for x in ABC:
    first = f'123{x}24'
    second = f'135{x}78'
    suma = int(first, 27) + int(second, 27)
    if suma % 26 == 0:
        print(x, suma//26)