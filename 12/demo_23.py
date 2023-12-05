def is_prime(number):
    k = 2
    while k*k < number and number % k != 0:
        k += 1
    return k*k > number


# print(is_prime(137))

# 36 -> 2, 3, 4, 6, 6, 9, 12, 18
# 25 -> 5, 5
# 17 -> no
# 32 -> 2, 4, 8, 16


for n in range(20):
    # n=5
    s = '>' + '0'*39 + '1'*n + '2'*39
    # s = '>' + '0'*9 + '1'*n + '2'*36 + '0'*30 + '2'*3
    # print(s)
    # print(s2)
        # while '52' or '2222' or '1122' in s:  fixme так нельзя это ошибка
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)  # TODO важно поставить в конце 1
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    suma = s.count('1')*1 + s.count('2')*2 + s.count('5')*5
    suma2 = sum(int(i) for i in s[:-1])
    suma3 = sum(map(int, s[:-1]))
    # if suma == 64:
    # print(s)
    # print(n, suma)
    if is_prime(suma):
        print(suma)