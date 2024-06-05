with open('demo_21.txt') as fin:
    S, N = map(int, fin.readline().split())
    # A = [int(fin.readline()) for i in range(N)]
    A = [int(i) for i in fin]
    A.sort()

suma = 0
i = 0
while suma + A[i] <= S:
    suma += A[i]
    i += 1
count = i
free = S - (suma-A[i-1])
maxi = max(i for i in A if i <= free)

print(count, maxi)