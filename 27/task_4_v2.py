with open('task_4_B.txt') as fin:
    K = int(fin.readline())
    N = int(fin.readline())
    A = [int(i) for i in fin]

s1 = s2 = s3 = -10**10
for i in range(2*K, N):
    s1 = max(s1, A[i-2*K])
    s2 = max(s2, s1+A[i-K])
    s3 = max(s3, s2+A[i])

print(s3)
# РЕШЕНИЕ на 1 БАЛЛ
# with open('task_4_A.txt') as fin:
#     K = int(fin.readline())
#     N = int(fin.readline())
#     A = [int(i) for i in fin]
#
# sum_max = -10**10
# for i in range(N-2*K):
#     for j in range(i+K, N-K):
#         for k in range(j+K, N):
#             suma = A[i]+A[j]+A[k]
#             sum_max = max(sum_max, suma)
#
# print(sum_max)
