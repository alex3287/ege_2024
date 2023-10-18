x1 = int(input())
x2 = int(input())
x3 = int(input())

k = 1
if x1 == x2 or x1 == x3:
    k += 1
if x2 == x3:
    k += 1

if k == 1:
    print(k-1)
else:
    print(k)