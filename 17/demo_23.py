A = [int(i) for i in open('test.txt')]
# print(A)
maxi_3 = -10_000
count = 0
maxi_suma = 0

# Находим максимальное окfнчивающееся на 3
for i in A:
    if i > maxi_3 and abs(i) % 10 == 3:
        maxi_3 = i
# print(maxi_3)

# Пары где одно число оканчивается на 3 и сумма квадратов >=
for i in range(len(A)-1):
    if (abs(A[i]) % 10 == 3 and abs(A[i+1]) % 10 != 3)\
            or (abs(A[i+1]) % 10 == 3 and abs(A[i]) % 10 != 3):
        if A[i]**2 + A[i+1]**2 >= maxi_3**2:
            print(A[i], A[i+1])
            count += 1
            maxi_suma = max(maxi_suma, (A[i]**2 + A[i+1]**2))

print(count, maxi_suma)