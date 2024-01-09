# из любой СС в 10-ю
# print(int('14', 7))  # 7 -> 10
# print(int('ff', 16))
# из 10-ой в любую другую
ABC = '0123456789ABCDEFG'


def ten_to_q(number, base):
    if number < base:
        return ABC[number]
    return ten_to_q(number//base, base) + ABC[number%base]


def ten_to_q2(number, base):
    result = ''
    while number != 0:
        digit = number % base
        result = ABC[digit] + result
        number //= base
    return result


def count_0(number, base):  # считает количество нулей в данном числе
    count = 0
    while number != 0:
        digit = number % base
        if digit == 0:
            count += 1
        number //= base
    return count


print(ten_to_q(98127346918277649, 2))
print(ten_to_q2(98127346918277649, 2))
print(count_0(128, 64))