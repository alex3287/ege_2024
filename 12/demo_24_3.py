for n in range(4, 10000):
    s = '5' + '2'*n
    # print(s, end=' -> ')
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    suma = s.count('1') + s.count('2')*2 + s.count('5')*5
    if suma == 64:
        print(n)
