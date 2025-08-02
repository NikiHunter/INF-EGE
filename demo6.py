from turtle import *


screensize(3000, 3000)
tracer(0)
left(90)
m = 20
for _ in range(9):
    forward(22 * m)
    right(90)
    forward(6 * m)
    right(90)
pu()
forward(1 * m)
right(90)
forward(5 * m)
left(90)
pd()
for _ in range(9):
    forward(53 * m)
    right(90)
    forward(75 * m)
    right(90)
pu()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * m, y * m)
        dot(5)
done()
