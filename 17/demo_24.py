A = [int(i) for i in open('17.txt')]

max_13 = max(i for i in A if i % 100 == 13)
# count = 0
# sum_max = -1
arr = []

for i in range(len(A)-2):
    suma = A[i] + A[i+1] + A[i+2]
    if ((99 < A[i] < 1000) + (len(str(A[i+1])) == 3) + (len(str(A[i+2])) == 3)) == 2:
        if suma <= max_13:
            arr.append(suma)
            # count += 1
            # sum_max = max(sum_max, suma)
            # print(A[i], A[i+1], A[i+2])

print(len(arr), max(arr))

