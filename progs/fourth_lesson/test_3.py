# n!   => 5! = 1*2*3*4*5 = 120

n = int(input('-> '))
factorial = 1

for i in range(1, n+1):
    # print(i, end=' ')
    factorial *= i

# print()
print(factorial)