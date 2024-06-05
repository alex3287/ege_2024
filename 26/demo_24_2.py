# def last_item(arr):
#     return arr[-1]

with open('demo_24.txt') as fin:
    N = int(fin.readline())
    A = [tuple(map(int, i.split())) for i in fin]
    # A.sort(key=last_item)
    A.sort(key=lambda tup: tup[1])

Conf = [A[0][1]]
for start, finish in A:
    if start >= Conf[-1]:
        Conf.append(finish)

pause = 0
for start, finish in A:
    if Conf[-2] <= start:
        pause = max(pause, start-Conf[-2])

print(len(Conf), pause)
