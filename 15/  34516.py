for A in range(20):
    flag = 1
    for x in range(2000):
        F = ((x&28 != 0) or (x&45 != 0)) <= ((x&48 == 0) <= (x&A != 0))
        if F == 0:
            flag = 0
            break
    if flag == 1:
        print(A)
