s = open('24-14100_14100.txt').readline()

A = ['ABA', "ABC", 'BCB']
B = ['CB', 'AC', 'BB', 'BA', 'AB']

for i in A:
    s=s.replace(i,"+++")
for j in B:
    s=s.replace(j,"++")

s=s.replace('A'," ").replace('B'," ").replace('C'," ")
maxi = max(len(i) for i in s.split())
print(maxi)

