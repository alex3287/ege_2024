s = open('test.txt').read()
A = [i for i in range(len(s)) if s[i] == 'T']
# maxi = max()
maxi = 0
for i in range(len(A)-101):
    maxi = max(maxi, (A[i+101] - A[i] - 1))

print(maxi)
