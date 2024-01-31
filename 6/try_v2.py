from turtle import *


color('green')
shape('turtle')
speed(30)
screensize(2048, 1980)
k=1
tracer(0)
left(90)

for i in range(2):
    fd(23*k)
    lt(90)
    bk(27*k)
    lt(90)
up()
bk(5*k)
rt(90)
fd(11*k)
lt(90)
down()
for i in range(2):
    fd(26*k)
    rt(90)
    fd(32*k)
    rt(90)

up()
count = 0
for x in range(11, 44):
    for y in range(-5, 22):
        goto(x*k, y*k)
        dot(5, 'red')
        count += 1

print(count, 28*24)
# 672
# -374
# 891
print(891+672-374)
done()