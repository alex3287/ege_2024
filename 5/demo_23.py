def alg(N):
    bin_number = bin(N)[2:]
    suma = bin_number.count('1')
    if suma % 2 == 0:
        bin_number = '10' + bin_number[2:] + '0' # 1100 => 1000
    else:
        bin_number = '11' + bin_number[2:] + '1'
    R = int(bin_number, 2) # перевод из 2 СС в 10 СС
    return R


# print(alg(6))
#
for N in range(10, 30):
    R = alg(N)
    if R > 40:
        print(N, '->', R)


# s = '12345678'
# print(s[3:])  # срезы классная тема (посмотри ее)
