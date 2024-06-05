s = open('test2.txt').read()
A = [i for i in range(len(s)) if s[i] == 'T']
print(max(A[i+101] - A[i] - 1 for i in range(len(A)-101)))
