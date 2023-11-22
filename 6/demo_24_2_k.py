from turtle import *


shape('turtle')  # принемает форму черепашки можно не писать
color('green')  # цвет зеленый можно не писать
tracer(0)  # отключает анимацию можно не писать
screensize(1800, 1800)  # дает возможность двигать холст
left(90)  # очень важно

for i in range(2):
    forward(8 * 30)
    right(90)
    forward(18 * 30)
    right(90)

up()
forward(4 * 30)
right(90)
forward(10 * 30)
left(90)
down()

for i in range(2):
    forward(17 * 30)
    right(90)
    forward(7 * 30)
    right(90)

up()  # поднимает перо и черепашка при движении не оставляет след
for x in range(19):
    for y in range(22):
        goto(x * 30, y * 30)
        dot(5, 'red')

done()

print(22 * 19 - 13 * 11)