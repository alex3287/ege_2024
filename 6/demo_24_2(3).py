from turtle import *


shape('turtle')
color('green')
screensize(1800, 1800)
tracer(0)
speed(300)
left(90)


for i in range(2):
    forward(8 * 30) # увеличиваем масштаб в 30 раз
    right(90)
    forward(18 * 30)  # увеличиваем масштаб в 30 раз
    right(90)
up()
forward(4 * 30)
right(90)
forward(10 * 30)
left(90)
down()
for i in range(2):
    forward(17 * 30)  # увеличиваем масштаб в 30 раз
    right(90)
    forward(7 * 30)  # увеличиваем масштаб в 30 раз
    right(90)


up()
for x in range(19):
    for y in range(22):
        goto(x * 30, y * 30) # увеличиваем масштаб в 30 раз
        dot(5, 'red')
done()

print(19 * 9 + 8 * 13)
print(19 * 22 - 11 * 13)
