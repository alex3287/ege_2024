def F(A, x):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))


for A in range(100):
    flag = 1
    for x in range(100):
        if F(A, x) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)