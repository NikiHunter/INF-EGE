from turtle import *


tracer(0)
screensize(5000, 5000)
m = 40

lt(255)
for _ in range(3):
    lt(30)
    for _ in range(4):
        fd(10 * m)
        lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
