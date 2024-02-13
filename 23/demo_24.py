def F(start, finish):
    if start > finish or start == 11:
        return 0
    if start == finish:
        return 1
    return F(start+1, finish) + F(start*2, finish) + F(start*start, finish)


print(F(2, 20))