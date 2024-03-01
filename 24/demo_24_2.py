s = open('test2.txt').read()
A = s.split('T')
maxi = 0
for i in range(len(A)-100):
    temp = 'T'.join(A[i:i+101])
    maxi = max(maxi, len(temp))
    # print(temp)
# print(A)
print(maxi)