def alg(N):
    bin_number = bin(N)[2:]
    if N % 3 == 0:
        bin_number += bin_number[-3:]
    else:
        bin_number += bin(N % 3 * 3)[2:]
    R = int(bin_number, 2)
    return R


# print(alg(4))
for N in range(10, 200):
    R = alg(N)
    if R > 151 and R < 167:
        print(f'N:{N} -> R:{R}')