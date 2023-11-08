from turtle import *


# shape('turtle')
# color('green')
tracer(0)
left(90)

for i in range(7):
    fd(10*30)
    rt(120)
up()
for x in range(10):
    for y in range(10):
        goto(x*30, y*30)
        dot(5, 'red')

done()