def F(start, finish):
    if start > finish or start == 17:
        return 0
    if start == finish:
        return 1
    return F(start+1, finish) + F(start*2, finish)


print(F(1, 10) * F(10, 35))
# print(F(7, 17))
# 7 - 14 - 15 - 16 -17
# 7 - 8 - 16 - 17
# 7 - 8 - 9 - 10 .... - 17