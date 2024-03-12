def devisions(number):
    suma = 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            suma = i + number // i
            break
    return suma


# def devisions2(number):
#     A = []
#     for i in range(2, number-1):
#         if number % i == 0:
#             A.append(i)
#     if A:
#         return max(A) + min(A)
#     return 0


for i in range(700_001, 1_000_000):
    M = devisions(i)
    if M % 10 == 8:
        print(i, M)