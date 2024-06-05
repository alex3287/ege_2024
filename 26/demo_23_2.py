with open('demo_23.txt') as fin:
    N = int(fin.readline())
    A = [int(i) for i in fin]

A.sort(reverse=True)

BOX = A[0]
count = 1
for box in A[1:]:
    if BOX - box >=3:
        count += 1
        BOX = box

print(count, BOX)