s = open('test_23.txt').read()
A = s.split('PP')
print(A)
print(max(len(i) for i in A)+2)