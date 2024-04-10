with open('p_119.txt') as fin:
    N, L, M = map(int, fin.readline().split())
    A = [i.split() for i in fin]
    A = [(int(i[0]), int(i[1]), i[2]) for i in A]
    A.sort()

parks = [0] * (L+M)
count_bus = count_car = 0
for start, time, type in A:
    if type == 'A':
        for i in range(L+M):
            if start >= parks[i]:
                parks[i] = start + time
                count_car += 1
                break
    else:
        for i in range(L, L + M):
            if start >= parks[i]:
                parks[i] = start + time
                count_bus += 1
                break

print(count_bus, N - count_car - count_bus)