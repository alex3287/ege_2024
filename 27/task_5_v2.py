from math import ceil


with open('task_5_A.txt') as fin:
    N, K, V = map(int, fin.readline().split())
    A = [tuple(map(int, i.split())) for i in fin]

min_sum = 10**10
for i in range(N):
    base_km = A[i][0]
    suma = 0
    for j in range(N):
        if i == j:
            continue
        km, volume = A[j]
        d1 = abs(base_km - km)
        d2 = K - d1
        suma += min(d1, d2) * ceil(volume / V)
    min_sum = min(min_sum, suma)

print(min_sum)