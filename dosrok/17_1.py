A = [int(i) for i in open('17_1.txt')]

count = 0
sum_max = 0

maxi_19 = max(x for x in A if x % 19 == 0)

for i in range(len(A)-1):
    if A[i] > maxi_19 or A[i+1] > maxi_19:
        count += 1
        sum_max = max(sum_max, A[i]+A[i+1])

print(count, sum_max)
