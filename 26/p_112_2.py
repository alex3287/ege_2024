with open('p_112.txt') as fin:
    N, M = map(int, fin.readline().split())
    A = [tuple(map(int, fin.readline().split())) for i in range(M)]
A.sort(key=lambda x: x[0])

banks = [0]*N
count_banks = [0]*N
last = 0
for start, time in A:
    for i in range(N):
        if start >= banks[i] and start <= 1440: #TODO убрать 15
             banks[i] = start+time
             count_banks[i] += 1
             last = i+1
             break
    else:
        time_min = min(banks)
        index = banks.index(time_min)
        if banks[index] <= 1440: #fixme
            banks[index] = time_min + time
            count_banks[index] += 1
            last = index + 1

print(sum(count_banks), last)