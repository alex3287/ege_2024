print('x y w z')
for x in range(2):
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                F = (y <= x) and (not z) and (w)
                if F == 1:
                    print(x, y, w, z)
