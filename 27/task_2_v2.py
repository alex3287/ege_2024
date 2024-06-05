with open('task_2_B.txt') as fin:
    N = int(fin.readline())
    A_sum = [10**10] * 43
    A_len = [0] * 43
    suma = sum_max = 0
    len_min = 10**10
    for i in range(N):
        x = int(fin.readline())
        suma += x
        d = suma % 43
        if d == 0:
            sum_max = suma
            len_min = i+1
        else:
            sum_temp = suma - A_sum[d]
            len_temp = i+1 - A_len[d]
            if sum_temp > sum_max or (sum_temp == sum_max and len_temp < len_min):
                sum_max = sum_temp
                len_min = len_temp
        if suma < A_sum[d]:
            A_sum[d] = suma
            A_len[d] = i+1
print(len_min)


# РЕШЕНИЕ на 1 БАЛЛ
# with open('task_2_A.txt') as fin:
#     N = int(fin.readline())
#     A = [int(i) for i in fin]
#
# sum_max = 0
# min_len = 10**10
#
# for i in range(N):
#     suma = 0
#     cur_len = 0
#     for j in range(i, N):
#         suma += A[j]
#         cur_len += 1
#         if suma % 43 == 0:
#             if suma > sum_max or (suma==sum_max and cur_len<min_len):
#                 sum_max = suma
#                 min_len = cur_len
#
# print(min_len)
