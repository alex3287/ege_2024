def alg(N):
    bin_number = bin(N)[2:]
    if N % 3 == 0:
        bin_number += bin_number[-3:]
    else:
        bin_number += bin(N % 3 * 3)[2:]
    R = int(bin_number, 2)
    return R


# print(alg(12))

for N in range(4, 200):
    R = alg(N)
    if R > 151 and R < 167:
        print(f'N:{N} -> R:{R}')



# s = '123456789'
# print(s[::-1])