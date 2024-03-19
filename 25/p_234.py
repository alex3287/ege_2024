def devisions(number):
    A = set()
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            A.add(i)
            A.add(number//i)
    return sorted(A)


for i in range(9_500_001, 9_600_001):
    R = devisions(i)
    if 0 < len(R) < 3:
        print(i-9500000, i, R)