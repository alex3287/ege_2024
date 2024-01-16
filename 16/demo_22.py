def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n-1)
    if n > 1 and n % 2 != 0:  # не нужно
        return 2 * F(n-2)


print(F(26))