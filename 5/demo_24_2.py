def alg(N):
    bin_number = bin(N)[2:]
    if N % 3 == 0:
        bin_number += bin_number[-3:]
    else:
        bin_number += bin(N % 3 * 3)[2:]
    R = int(bin_number, 2)
    return R


# print(alg(15))  # 100

for N in range(12, 200):
    R = alg(N)
    if R > 151 and R < 167:
        print(N, '->', R)


# s = '12345678'
# print(s[3:])  # срезы классная тема (посмотри ее)
