def is_prime(number):
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True


def is_prime_2(number):
    k = 2
    while k*k < number and number % k != 0:
        k += 1
    return k*k > number



# 36 -> 2, 3, 4, 6, 6, 9, 12, 18

for n in range(15):
    s = '>' + '0'*39 + '1'*n + '2'*39
    # s = '>' + '2'*30 + '0'*3 + '1'*n + '2'*9 + '0'*36

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    # print(s)
    # suma = s.count('1') + s.count('2')*2 + s.count('5')*5
    suma2 = sum(int(i) for i in s[:-1])
    suma3 = sum(map(int, s[:-1]))
    # if suma == 64:
    print(n, suma2, is_prime_2(suma2), is_prime(suma3))