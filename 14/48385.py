ABC = '0123456789abc'
for x in ABC:
    for y in ABC:
        first = f'8{x}78{y}'
        second = f'79{x}{y}7'
        suma = int(first, 13) + int(second, 18)
        # if suma % 18 == 0:
        print(first, second, suma, suma/9)