def alg(N):
    bin_num = bin(N)[2:]
    if N % 3 == 0:
        bin_num += bin_num[-3:]
    else:
        temp = bin(N % 3 * 3)[2:]
        bin_num += temp
    R = int(bin_num, 2)
    return R


for N in range(13, 100):
    R = alg(N)
    if R > 151 and R < 167:
        print(f'{N} -> {R}')