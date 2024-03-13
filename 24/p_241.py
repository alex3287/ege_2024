# согл+согл+гл
s = open('24-241.txt').readline()
s = s.replace('C', 'B').replace('D', 'B').replace('F', 'B')
s = s.replace('E', 'A').replace('O', 'A')
s = s.replace('BBA','+')
s = s.replace('A', ' ').replace('B', ' ')
maxi = max(len(i) for i in s.split())
print(maxi)