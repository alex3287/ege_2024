with open('p_112.txt') as fin:
    N, M = map(int, fin.readline().split())
    A = [tuple(map(int, i.split())) for i in fin]

A.sort(key=lambda x: x[0])

banks = [0] * N
count_banks = [0] * N
last = 0
for i in range(M):
    start, time = A[i]
    for j in range(N):
        if start >= banks[j] and start <= 1440: #fixme поменяй 15
            banks[j] = start+time
            count_banks[j] += 1
            last = j+1
            break
    else:
        min_time = min(banks)
        for j in range(N):
            if min_time <= 1440 and min_time == banks[j]: #TODO
                banks[j] = min_time + time
                count_banks[j] += 1
                last = j + 1
                break

print(sum(count_banks), last)
