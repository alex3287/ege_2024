with open('task_1_A.txt') as fin:
    N = int(fin.readline())
    A = [tuple(map(int, i.split())) for i in fin]

Sums = []
suma = 0
for i in A:
    suma += max(i)

Sums.append(suma)
for i in range(N):
    suma = 0
    for j in range(N):
        if i == j:
            suma += min(A[j])
        else:
            suma += max(A[j])
    Sums.append(suma)

print(Sums)
print(max(i for i in Sums if i % 3 != 0))
