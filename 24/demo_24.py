s = open('test2.txt').read()
A = s.split('T')

maxi = 0
for i in range(len(A)-3):
    temp = 'T'.join(A[i:i+4])
    maxi = max(len(temp), maxi)
    # print(temp)
print(maxi)