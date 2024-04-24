with open('task_1_B.txt') as fin:
    N = int(fin.readline())
    A = [tuple(map(int, i.split())) for i in fin]

suma_max = 0
S = []
for i in A:
    suma_max += max(i)


for a, b in A:
    suma = suma_max - abs(a-b)
    S.append(suma)

print(max(i for i in S if i % 3 != 0))