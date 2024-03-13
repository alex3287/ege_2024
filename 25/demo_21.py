def devisions(number):
    A = set()
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            A.add(i)
            A.add(number//i)
            if len(A) > 2:
                A.add(0)
                return A
    return A



def devisions2(number):
    A = set()
    for i in range(2, number):
        if number % i == 0:
            A.add(i)
            A.add(number//i)
    return A

for i in range(174457, 174506):
# for i in range(1, 11):
    R = devisions(i)
    if len(R) == 2:
        print(R)

