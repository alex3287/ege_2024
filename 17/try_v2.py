A = [int(i) for i in open('try.txt')]
# print(A)
count = 0
maxi_21 = -1000000
maxi_sum = -10000000000
for i in A:
    if abs(i) % 100 == 21:
        maxi_21 = max(maxi_21, i)
# print(maxi_21)

for i in range(len(A)-1):
    suma = A[i]**2 + A[i+1]**2
    suma2 = A[i] + A[i+1]
    # print(i, (len(str(abs(A[i]))) == 5 and abs(A[i]) % 100 == 21) + (abs(A[i+1]) % 100 == 21 and len(str(abs(A[i]))) == 5))
    if (len(str(abs(A[i]))) == 5 and abs(A[i]) % 100 == 21) + (abs(A[i+1]) % 100 == 21 and len(str(abs(A[i+1]))) == 5) == 1:
        if suma >= maxi_21**2:
            print(A[i], A[i+1])
            count += 1
            maxi_sum = max(maxi_sum, suma2)
print(count, maxi_sum)
