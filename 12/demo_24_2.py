for n in range(4, 100):
    s = '5' + '2'*n

    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    # print(s)
    suma = s.count('1') + s.count('2')*2 + s.count('5')*5
    suma2 = sum(int(i) for i in s)
    suma3 = sum(map(int, s))
    # if suma == 64:
    print(n, suma, suma2, suma3)