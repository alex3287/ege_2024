A = [int(i) for i in open('demo_23.txt')]
# print(A)
max_3 = -10000
sum_max_sq = 0
count = 0
# поиск максимального оканчивающегося на 3
for i in A:
    if abs(i) % 10 == 3:
        max_3 = max(max_3, i)
# print(max_3)
#  работа с парами элементов
for i in range(len(A)-1):
    sum_sq = A[i]**2 + A[i+1]**2
    if (abs(A[i]) % 10 == 3 and abs(A[i+1]) % 10 != 3) \
        or (abs(A[i+1]) % 10 == 3 and abs(A[i]) % 10 != 3):
        if sum_sq >= max_3**2:
            count += 1
            sum_max_sq = max(sum_max_sq, sum_sq)
            print(A[i], A[i+1])

print(count, sum_max_sq)
