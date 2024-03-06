from turtle import *


shape('turtle')
color('green')
screensize(2400, 2400)
tracer(0)
left(90)

for i in range(10):
    fd(15*40)
    rt(60)
up()
for x in range(28):
    for y in range(-8, 24):
        goto(x*40, y*40)
        dot(3, 'red')

done()
