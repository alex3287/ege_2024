def ten_to3(number):
    if number == 0: return '0'
    result = ''
    while number:
        result = str(number % 3) + result
        number //= 3
    return result


def alg(N):
    num_3 = ten_to3(N)

    if N % 4 == 0:
        num_3 += num_3[-3:]
    else:
        num_3 += ten_to3(N % 4 * 4)

    R = int(num_3, 3)
    return R


# print(alg(16)) #121121
# print(int('121121', 3)) #12211
for N in range(0, 100):
    R = alg(N)
    if R < 127 and R > 120:
        print(f'N:{N} -> R:{R}')