from math import ceil

with open('task_5_A.txt') as fin:
    N, K, V = map(int, fin.readline().split())
    A = [tuple(map(int, i.split())) for i in fin]

L = []

for i in range(N):
    lab_km = A[i][0]
    suma = 0
    for j in range(N):
        if i == j:
            continue
        km, volume = A[j]
        distance = min(abs(km - lab_km), K - abs(km-lab_km))
        suma += distance * ceil(volume / V)
    L.append(suma)

print(min(L))