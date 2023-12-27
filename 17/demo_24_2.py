A = [int(i) for i in open('17.txt')]
# print(A)
max_13 = max(i for i in A if i % 100 == 13)
# print(max_13)
count = 0
sum_max = 0
# Trash = []
for i in range(len(A)-2):
    suma = sum(A[i:i+3])
    first = len(str(A[i])) == 3
    second = 99 < A[i+1] < 1000
    third = len(str(A[i+2])) == 3
    if first + second + third == 2 and suma <= max_13:
        print(A[i:i+3])
        # Trash.append(suma)
        count += 1
        sum_max = max(sum_max, suma)

print(count, sum_max)
# print(len(Trash), max(Trash))
