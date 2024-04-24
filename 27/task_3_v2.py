from math import ceil


with open('task_3_A.txt') as fin:
    N, K = map(int, fin.readline().split())
    A = [tuple(map(int, i.split())) for i in fin]

sum_min = 10**10
for i in range(N):
    lab_km = A[i][0]
    suma = 0
    for j in range(N):
        if i == j:
            continue
        km, bottle = A[j]
        suma += abs(km-lab_km) * ceil(bottle/K)
    sum_min = min(sum_min, suma)
print(sum_min)