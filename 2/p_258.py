print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in range(2):
            for w in 0,1:
                F = not((((not w) <= (not y)) <= (not z)) <= x)
                if F == 0:
                    print(x, y, z, w)


# A -> B ==== A <= B === not A or B