with open('task_2_A.txt') as fin:
    N = int(fin.readline())
    A = [int(i) for i in fin]

sum_max = 0
min_len = 10**10

for i in range(N):
    suma = 0
    cur_len = 0
    for j in range(i, N):
        suma += A[j]
        cur_len += 1
        if suma % 43 == 0:
            if suma > sum_max or (suma==sum_max and cur_len<min_len):
                sum_max = suma
                min_len = cur_len

print(min_len)
