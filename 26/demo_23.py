with open('demo_23.txt') as fin:
    N = int(fin.readline())
    A = [int(x) for x in fin]
    A.sort(reverse=True)

Boxes = [A[0]]
for box in A[1:]:
    if Boxes[-1] - box >= 3:
        Boxes.append(box)

print(len(Boxes), Boxes[-1])

