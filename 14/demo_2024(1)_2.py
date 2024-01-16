# перевод из любой СС в 10-ю
# print(int('ff', 16))

# перевод из 10-й СС в 2,8,16
# print(f'255 ->  16:{255:x}, 8:{255:o}, 2:{255:b}')

# первод из 10-й в любую другую
ABC = '0123456789ABCDEFGH'

def ten_to_q(number, base):  # функция первода из 10-й в любую другую
    if number < base:
        return ABC[number]
    return ten_to_q(number//base, base) + ABC[number%base]

# print(ten_to_q(29, 3))
# print(int('1002', 3))

def count_0(number):   # подсчитывает кол-во нулей в 64-ой системе счисления
    count = 0
    while number != 0:
        if number % 64 == 0:   # если нужна другая СС, то поменяйте 64 на нужное значение
            count += 1
        number //= 64   # если нужна другая СС, то поменяйте 64 на нужное значение
    return count


# print(count_0(64))

#  Демоверсия 2024
ABC2 = '0123456789abcdefghi'
for x in ABC2:
    first = f'98897{x}21'
    second = f'2{x}923'
    suma = int(first, 19) + int(second, 19)
    if suma % 18 == 0:
        print(x, suma/18)
