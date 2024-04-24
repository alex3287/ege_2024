with open('task_4_A.txt') as fin:
    K = int(fin.readline())
    N = int(fin.readline())
    A = [int(i) for i in fin]

sum_max = -10**10
for i in range(N-2*K):
    for j in range(i+K, N-K):
        for k in range(j+K, N):
            suma = A[i]+A[j]+A[k]
            sum_max = max(sum_max, suma)

print(sum_max)
