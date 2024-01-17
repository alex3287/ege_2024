# Генерация строки
# for n in range(11):
#     s = '1'*7 + '3'*n + '4'*5
#     print(s)

# Используем замену
# s = '2'*10
# print(s)
# s = s.replace('222', '+', 1)
# print(s)

for n in range(4, 10_000):
    s = '5' + '2'*n
    # print(s, '->', end=' ')

    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    # suma = s.count('1') + s.count('2')*2 + s.count('5')*5
    suma2 = sum(map(int, s))  # считает сумму цифр в строке
    if suma2 == 64:
        print(s, suma2, n)





