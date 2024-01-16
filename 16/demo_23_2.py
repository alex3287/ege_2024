from sys import setrecursionlimit, set_int_max_str_digits


setrecursionlimit(3000)
# set_int_max_str_digits(0)
def F(n):
    if n == 1:
        return 1
    return n * F(n-1)


print(F(2023))