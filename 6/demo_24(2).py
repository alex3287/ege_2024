from turtle import *


shape('turtle')
color('green')
left(90)
tracer(0)

for i in range(7):
    forward(10 * 30)
    right(120)
up()

for x in range(10):
    for y in range(11):
        goto(x * 30, y * 30)
        dot(5, 'red')
done()