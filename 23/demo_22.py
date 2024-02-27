def F(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    return F(start+1, finish) + F(start*2, finish)


print(F(1, 10) * F(10, 20))