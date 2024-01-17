def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for n in range(28):
    s = '>' + '0'*39 + '1'*n + '2'*39
    # s2 = '>' + '0'*9 + '1'*n + '2'*39 + '0'*30
    # print(s, '->', end=' ')
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    # suma = sum(map(int, s[:-1]))
    # print(s, suma)
    print(n,'->', s.count('1') + s.count('2')*2, is_prime(s.count('1') + s.count('2')*2))
