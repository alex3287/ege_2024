def alg(N):
    oct_num = oct(N)[2:]
    oct_new = ''
    for i in oct_num:
        if int(i) % 2 == 0:
            oct_new += '1'
        else:
            oct_new += i
    oct_new += str(N % 8)
    R = int(oct_new, 8)

    return R


for i in range(1000, 10000):
    R = alg(alg(i))
    if R % 234 == 0:
        print(R)