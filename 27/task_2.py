# РЕШЕНИЕ НА 2 БАЛЛА
with open('task_2_A.txt') as fin:
    N = int(fin.readline())
    A_sum = [10**30] * 43
    A_len = [0] * 43
    sum_max = cur_ln = suma = 0
    min_ln = 10**10

    for i in range(N):
        x = int(fin.readline())
        suma += x
        d = suma % 43
        if d == 0:
            sum_max = suma
            min_ln = i+1
        else:
            sum_tmp = suma - A_sum[d]
            cur_ln = i+1 - A_len[d]
            if sum_tmp > sum_max or (sum_tmp == sum_max and cur_ln < min_ln):
                sum_max = sum_tmp
                min_ln = cur_ln
        if suma < A_sum[d]:
            A_sum[d] = suma
            A_len[d] = i+1

print(min_ln)


# РЕШЕНИЕ НА 1 БАЛЛ
# with open('task_2_A.txt') as fin:
#     N = int(fin.readline())
#     K = 43
#     A = [int(i) for i in fin]
#     max_sum = 0
#     min_count = 10000000000
#
# for i in range(N): # fixme
#     suma = 0
#     count = 0
#     for j in range(i, N):
#         suma += A[j]
#         count += 1
#         if suma % K == 0:
#             if suma > max_sum or (suma == max_sum and count < min_count):
#                 max_sum, min_count = suma, count
#
# print(min_count)