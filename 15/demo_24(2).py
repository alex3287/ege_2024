for A in range(200):
    flag = 1
    for x in range(400):
        for y in range(400):
            F = (x + 2*y < A) or (y > x) or (x > 60)
            if F == 0:
                flag = 0
                break
    if flag == 1:
        print(A)