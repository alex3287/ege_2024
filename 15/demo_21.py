def F(A, x):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))


for A in range(1, 100):
    flag = 1
    for x in range(1, 100):
        if F(A, x) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)