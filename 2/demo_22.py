print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in range(2):
            for w in 0,1:
                F = not(y <= (x == w)) and (z <= x)
                if F == 1:
                    print(x, y, z, w)
