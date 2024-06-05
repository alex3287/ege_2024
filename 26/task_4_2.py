with open('p_111.txt') as fin:
    K = int(fin.readline())
    N = int(fin.readline())
    A = [tuple(map(int, i.split())) for i in fin]
    A.sort()

Camera = [0]*K
count = last = 0
for start, finish in A:
    for j in range(K):
        if start > Camera[j]:
            Camera[j] = finish
            count += 1
            last = j+1
            break

print(count, last)