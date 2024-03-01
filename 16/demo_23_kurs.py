from sys import setrecursionlimit, set_int_max_str_digits
setrecursionlimit(2050)
set_int_max_str_digits(0)


def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)


print(F(2023)/ F(2020))