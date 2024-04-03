with open('demo_24.txt') as fin:
    N = int(fin.readline())
    A = [tuple(map(int, x.split())) for x in fin]
    A.sort(key=lambda tup: tup[1])

Conf = [A[0][1]]
for start, finish in A:
    if start >= Conf[-1]:
        Conf.append(finish)

pause = 0
for start, finish in A:
    if Conf[-2] <= start:
        pause = max(pause, start - Conf[-2])

print(len(Conf), pause)

