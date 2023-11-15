def add(x, y):
    suma = x + y
    return suma


def sum_odd_items(A):
    suma = 0
    for i in A:
        if i % 2 != 0:
            suma += i
    return suma


a, b = map(int, input().split())
print(add(a, b))
print(add(34, 5))
print(sum_odd_items([2,3,4,5,6,7,8]))