s = open('24.txt').read()
s = s.replace('O', 'A')
s = s.replace('C', 'F').replace('D','F')
s = s.replace('FA', '+')

maxi = 0
for i in range(150):
    template = '+'*i
    if template in s:
        print(i)
    else:
        print('Done')
        break