from turtle import *


shape('turtle')
color('green')
tracer(0)
left(90)

for i in range(7):
    forward(10 * 30) # увеличиваем масштаб в 30 раз
    right(120)

up()
for x in range(10):
    for y in range(11):
        goto(x * 30, y * 30) # увеличиваем масштаб в 30 раз
        dot(14, 'red')
done()

