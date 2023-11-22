from turtle import *


shape('turtle')  # принемает форму черепашки можно не писать
color('green')  # цвет зеленый можно не писать
tracer(0)  # отключает анимацию можно не писать
left(90)  # очень важно

for i in range(7):
    forward(10 * 30)
    right(120)

up()  # поднимает перо и черепашка при движении не оставляет след
for x in range(10):
    for y in range(11):
        goto(x * 30, y * 30)
        dot(5, 'red')

done()