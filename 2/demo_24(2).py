print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                F = (x and not y) or (y == z) or (not w)
                if F == 0:
                    print(x, y, w, z)
