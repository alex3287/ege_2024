def alg(N):
    bin_number = f'{N:2b}'

    suma = bin_number.count('1') #101010
    bin_number += str(suma % 2)

    suma = bin_number.count('1')  # 101010
    bin_number += str(suma % 2)

    R = int(bin_number, 2)
    return R


print(alg(13))