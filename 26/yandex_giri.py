with open('test.txt') as fin:
    N = int(fin.readline())
    A = [int(x) for x in fin]
    A.sort()
    print(A)

suma = 0
for i in range(1, 25):
    for j in range(N):
        if i in A:
            break
