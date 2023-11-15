def alg(N):
    bin_number = bin(N)[2:]
    suma = bin_number.count('1')
    bin_number += str(suma % 2)

    suma = bin_number.count('1')
    bin_number += str(suma % 2)
    R = int(bin_number, 2)
    return R


# print(alg(28))
for N in range(4, 200):
    R = alg(N)
    # if R > 151 and R < 167:
    print(f'N:{N} -> R:{R}')