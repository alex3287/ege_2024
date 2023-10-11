print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (w or x or y) <= ((y or z) and x or y and (w or z))
                if F == 0:
                    print(x, y, z, w)