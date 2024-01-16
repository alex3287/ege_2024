def F(n):
    if n > 2024:
        return n
    return n * F(n+1)


print(F(2022)/F(2024))