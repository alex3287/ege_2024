s = open('demo_23.txt').read()
s = s.replace('O', 'A').replace('C', 'F').replace('D', 'F')
s = s.replace('FA', '+')
for x in range(200):
    template = '+'*x
    if template in s:
        print(x)
   
# print(s)