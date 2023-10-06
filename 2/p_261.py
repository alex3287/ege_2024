print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in range(2):
            for w in 0,1:
                F1 = (not w or y) == (z <= x)
                if F1 == 1:
                    print(x, y, z, w)
print()
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in range(2):
            for w in 0,1:
                F2 = (w <= y) and ((not x) == z)
                if F2 == 0:
                    print(x, y, z, w)