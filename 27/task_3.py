from math import ceil

with open('task_3_B.txt') as fin:
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
    B[i] += B[i-1] + A[i][1]
print(B)

lab_1 = 0
for i in range(1, N):
    lab_1 += (A[i][0] - A[0][0]) * A[i][1]
print(lab_1)

min_lab = lab_1
for i in range(1, N):
    distance = A[i][0] - A[i-1][0]
    lab_1 = lab_1 + distance * B[i-1] - distance * (B[-1]-B[i-1])
    min_lab = min(min_lab, lab_1)

print(min_lab)

# with open('task_3_A.txt') as fin:
#     N, K = map(int, fin.readline().split())
#     A = [tuple(map(int, i.split())) for i in fin]
#
# L = []
#
# for i in range(N):
#     lab_km = A[i][0]
#     suma = 0
#     for j in range(N):
#         if i == j:
#             continue
#         km, bottle = A[j]
#         suma += abs(km - lab_km) * ceil(bottle / K)
#     L.append(suma)
#
# print(min(L))