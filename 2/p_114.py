print('a b c')
for a in 0,1:
    for b in 0,1:
        for c in range(2):
            F = (not a) or (b and not c)
            if F == 0:
                print(a, b, c)

# a ^ b = c
# (a and b) == c