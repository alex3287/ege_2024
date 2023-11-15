from turtle import *


screensize(1400, 1400)
# up()
# goto(-300, -300)
# down()
shape('turtle')
color('green')
tracer(0)
left(90)
mult = 30

for i in range(2):
    fd(8*mult)
    rt(90)
    fd(18 * mult)
    rt(90)

up()
fd(4*mult)
rt(90)
fd(10*mult)
lt(90)
down()
for i in range(2):
    fd(17*mult)
    rt(90)
    fd(7*mult)
    rt(90)
up()
for x in range(19):
    for y in range(22):
        goto(x*mult, y*mult)
        dot(5, 'red')

done()
print(19*22 - 13*11)
