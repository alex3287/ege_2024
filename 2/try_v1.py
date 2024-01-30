from itertools import *


def F(x, y, z, w):
    return w and (not x or y) and (not y and z or y and not z)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 0, a1, a2), (a3, 0, 0, 1), (1, a4, 0, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
