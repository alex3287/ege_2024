# вариант со сплитом
# s = open('test.txt').readline()
# s = s.replace('A', ' A').replace('B', 'B ')
# A = [i for i in s.split()]
# count = 0
# for i in A:
#     if i[0]=='A' and i[-1] == 'B' and len(i) >= 20:
#         count += 1
# print(count)
s = open('24-191.txt').read()
# print(s)
index_A = -1
count = 0
for i in range(len(s)):
    if s[i] == 'A':
        index_A = i
    elif s[i] == 'B' and index_A != -1:
        if i - index_A + 1 >= 20:
            count += 1
        index_A = -1
print(count)
