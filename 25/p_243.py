def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def devisions(number):
    A = set()
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            if is_prime(i):
                A.add(i)
            if is_prime(number//i):
                A.add(number//i)
    return A


for i in range(100_000, 500_000):
    R = devisions(i)
    if len(R)>3:
        A = sorted(R)
        step = A[1]-A[0]
        for j in range(1, len(A)-1):
            if A[j+1] - A[j] != step:
                break
        else:
            print(i, len(A)*step)
