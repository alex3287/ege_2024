# Для узла с IP-адресом 115.181.92.48 адрес сети равен 115.181.80.0. Чему равно
# значение третьего слева байта маски? Ответ запишите в виде десятичного
# числа

print(f'{92:b}')
print(f'{80:b}')

# 01011100
# 11110000
# 01010000
print(int('11110000', 2))
import functools