# сумма первых n чисел натурального ряда

n = int(input('-> '))
suma = 0

for i in range(1, n+1):
    print(i, end=' ')
    suma += i

print()
print(suma)

# print(1, '+', 2, '=', sep='')