from turtle import *


shape('turtle')
color('green')
left(90)
screensize(1600, 1600)
tracer(0)

for i in range(2):
    fd(8 * 30)
    right(90)
    fd(18 * 30)
    right(90)
up()
fd(4*30)
rt(90)
fd(10*30)
lt(90)
down()

for i in range(2):
    fd(17*30)
    rt(90)
    fd(7 * 30)
    rt(90)

up()
for x in range(19):
    for y in range(22):
        goto(x * 30, y * 30)
        dot(5, 'red')
done()

print(19 * 22 - 13 * 11)