with open('demo_21.txt') as fin:
    S, N = map(int, fin.readline().split())
    A = [int(x) for x in fin]
    A.sort()

suma = 0
count = 0
i=0
while suma + A[i] <= S:
    suma += A[i]
    i += 1
count = i

item = S - (suma - A[i-1])
maxi = max(i for i in A if i <= item)
print(count, maxi)