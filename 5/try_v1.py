def alg(N):
    bin_num = bin(N)[2:]
    if N % 2 == 0:
        bin_num += bin_num[-2:]
    else:
        bin_num = '1' + bin_num + '0'
    R = int(bin_num, 2)
    return R

# print(alg(10))
for N in range(10, 100):
    R = alg(N)
    # if R == 202:
    print(f'N:{N} -> R:{R}')