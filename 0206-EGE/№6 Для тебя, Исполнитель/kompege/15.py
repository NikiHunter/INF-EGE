from turtle import *


tracer(0)
screensize(5000, 5000)
m = 20

rt(270)
for _ in range(2):
    fd(23 * m)
    lt(90)
    bk(27 * m)
    lt(90)
up()
bk(5 * m)
right(90)
fd(11 * m)
left(90)
down()
for _ in range(2):
    fd(26 * m)
    right(90)
    forward(32 * m)
    right(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
print((23 + 1) * (27 + 1) + (26 + 1) * (32 + 1) - (27 - 11 + 1) * (23 - 2 + 1))
mainloop()
