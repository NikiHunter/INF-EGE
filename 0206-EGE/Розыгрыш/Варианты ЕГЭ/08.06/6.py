from turtle import *


tracer(0)
screensize(5000, 5000)
m = 10
for _ in range(9):
    forward(22 * m)
    right(90)
    forward(6 * m)
    right(90)
up()
forward(1 * m)
right(90)
forward(5 * m)
left(90)
down()
for _ in range(9):
    forward(53 * m)
    right(90)
    forward(75 * m)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
print(21 * 2 + 1 * 2)
mainloop()
