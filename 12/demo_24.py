for n in range(4, 10000):
    s = '5' + '2'*n
    # print(s)

    # while '52' or '2222' or '1122' in s:  fixme так нельзя это ошибка
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)  # TODO важно поставить в конце 1
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    suma = s.count('1')*1 + s.count('2')*2 + s.count('5')*5
    suma2 = sum(int(i) for i in s)
    suma3 = sum(map(int, s))
    if suma == 64:
        print(s)
        print(n, suma)