for A in range(1, 110):
    # flag = 1
    for x in range(1, 500):
        F = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)
        if F == 0:
            # flag = 0
            break
    else:
        print(A)
    # if flag == 1:
    #     print(A)