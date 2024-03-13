s = open('24-241.txt').readline()

# разбиваем строку
t = s.split('E')[1:-1]
mini = 1000000000
for i in t:
    if len(i) > 7 and i.count('B') == 2 and i.count('A') > 5:
        temp = i.split('B')
        if temp[1].count('A') > 5:
            mini = min(mini, len(i)+2)
print(mini)

# тут оказалось сложно, но можно подумать
# A = [0]*len(s)
# index_E = -1
# for i in range(len(s)):
#     if s[i] == 'E':
#         count_E = i
#     elif s[i] == 'B':
#         pass
#
#     if count_E == 1:
#         A[i] += 1
#
