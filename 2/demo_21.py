print('x y w z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                F = (x or y) and not (y == z) and (not w)
                if F:
                    print(x, y, w, z)