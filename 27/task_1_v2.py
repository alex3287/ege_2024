with open('task_1_B.txt') as fin:
    N = int(fin.readline())
    suma = 0
    sub_min = 10**10
    for i in range(N):
        a, b = map(int, fin.readline().split())
        sub = abs(a-b)
        if sub % 3:
            sub_min = min(sub_min, sub)
        suma += max(a, b)
print(suma)
if suma % 3 == 0:
    suma -= sub_min
print(suma)

# РЕШЕНИЕ на 1 БАЛЛ
# with open('task_1_A.txt') as fin:
#     N = int(fin.readline())
#     A = [tuple(map(int, i.split())) for i in fin]
#
# Sums = []
# suma = 0
# for i in A:
#     suma += max(i)
#
# Sums.append(suma)
# for i in range(N):
#     suma = 0
#     for j in range(N):
#         if i == j:
#             suma += min(A[j])
#         else:
#             suma += max(A[j])
#     Sums.append(suma)
#
# print(Sums)
# print(max(i for i in Sums if i % 3 != 0))
