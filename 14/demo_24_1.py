# перевод в десятичную int('2343', 5)
# перевод из десятичной bin, oct , hex
# 0, i
# 0123456789abcdefght  => 19 CC
from string import *
# print(ascii_letters)

ABC = '0123456789abcdefghi'
for x in ABC:
    first = f'98897{x}21'
    second = f'2{x}923'
    suma = int(first, 19) + int(second, 19)
    if suma % 18 == 0:
        print(first, second, suma, suma/18)

