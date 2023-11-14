def alg(N):
    bin_number = bin(N)[2:]
    suma = bin_number.count('1')
    bin_number += str(suma % 2)

    suma = bin_number.count('1')
    bin_number += str(suma % 2)
    R = int(bin_number, 2)
    return R


for N in range(10, 77):
    R = alg(N)
    if R > 77:
        print(f'N:{N} -> R:{R}')







print(alg(28))  #110