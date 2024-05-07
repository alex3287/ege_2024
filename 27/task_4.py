with open('task_4_B.txt') as fin:
    K = int(fin.readline())
    N = int(fin.readline())
    A = [int(i) for i in fin]

max_sum = -10**10
m1 = m2 = m3 = 0
for i in range(2*K, N):
    m1 = max(m1, A[i-2*K])
    m2 = max(m2, m1+A[i-K])
    m3 = max(m3, m2+A[i])

print(m3)


# Решение на 1 балл
# with open('task_4_A.txt') as fin:
#     K = int(fin.readline())
#     N = int(fin.readline())
#     A = [int(i) for i in fin]
#
# max_sum = -10**10
#
# for i in range(N-2*K):
#     for j in range(i+K, N-K):
#         for k in range(j+K, N):
#             suma = A[i] + A[j] + A[k]
#             max_sum = max(max_sum, suma)
#
# print(max_sum)
