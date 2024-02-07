# перевод из любой СС в 10 СС int('34a', 16)
# перевод из 10 в 2, 8, 16 => bin(x), oct, hex

ABC = '0123456789abcdefghi'
for x in ABC:
    first = f'98897{x}21'
    second = f'2{x}923'
    suma = int(first, 19) + int(second, 19)
    # if suma % 18 == 0:
    print(first, second, suma, suma/18)
