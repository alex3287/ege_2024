def alg(N):
    bin_number = bin(N)[2:]
    suma = bin_number.count('1')
    if suma % 2 == 0:
        bin_number = '10' + bin_number[2:] + '0'
    else:
        bin_number = '11' + bin_number[2:] + '1'
    R = int(bin_number, 2)
    return R


# print(alg(4))
for N in range(4, 40):
    R = alg(N)
    if R > 40:
        print(f'N:{N} -> R:{R}')