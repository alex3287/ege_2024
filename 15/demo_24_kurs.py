def F(A, x, y):
    return (x + 2*y < A) or (y > x) or (x > 60)


for A in range(200):
    flag = 1
    for x in range(200):
        for y in range(200):
            if F(A, x, y) == 0:
                flag = 0
                break
    if flag == 1:
        print(A)