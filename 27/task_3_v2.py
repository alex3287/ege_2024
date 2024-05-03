from math import ceil


with open('test.txt') as fin:
    N, K = map(int, fin.readline().split())
    A = []
    for i in range(N):
        km, bottle = map(int, fin.readline().split())
        box = ceil(bottle / K)
        A.append((km, box))
A.sort()
print(A)

B = [0]*N
B[0] = A[0][1]
for i in range(1, N):
    B[i] = B[i-1] + A[i][1]
print(B)

sum_0 = 0
for i in range(1, N):
    sum_0 += (A[i][0] - A[0][0]) * A[i][1]
print(sum_0)

sum_min = sum_0
for i in range(1, N):
    distance = A[i][0] - A[i-1][0]
    sum_0 = sum_0 + distance * B[i-1] - distance * (B[-1] - B[i-1])
    sum_min = min(sum_min, sum_0)

print(sum_min)

# РЕШЕНИЕ на 1 БАЛЛ
# from math import ceil
#
#
# with open('task_3_A.txt') as fin:
#     N, K = map(int, fin.readline().split())
#     A = [tuple(map(int, i.split())) for i in fin]
#
# sum_min = 10**10
# for i in range(N):
#     lab_km = A[i][0]
#     suma = 0
#     for j in range(N):
#         if i == j:
#             continue
#         km, bottle = A[j]
#         suma += abs(km-lab_km) * ceil(bottle/K)
#     sum_min = min(sum_min, suma)
# print(sum_min)