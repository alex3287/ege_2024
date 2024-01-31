from itertools import *


def F(x, y, z, w):
    return not(x or y) and not w or not (z or w) and y


for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    table = [(a1, 1, a2, a3), (a4, a5, 1, a6), (a7, 1, a8, 1)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if [F(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)