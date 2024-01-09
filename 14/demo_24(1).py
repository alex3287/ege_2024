ABC = '0123456789ABCDEFGHI'

for x in ABC:
    first = f'98897{x}21'
    second = f'2{x}923'
    suma = int(first, 19) + int(second, 19)
    if suma % 18 == 0:
        print(x, suma // 18)
