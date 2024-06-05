with open('p_111.txt') as fin:
    K = int(fin.readline())
    N = int(fin.readline())
    A = [tuple(map(int, x.split())) for x in fin]
    A.sort()
print(A)

Camera = [0]*K
count = last = 0
for start, finish in A:
    for j in range(K):
        if Camera[j] < start:
            Camera[j] = finish
            count += 1
            last = j+1
            break

print(count, last)