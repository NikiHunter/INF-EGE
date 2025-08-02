from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30

rt(270)
for _ in range(8):
    fd(10 * m)
    rt(45)
    fd(10 * m)
    rt(135)
for _ in range(4):
    fd(4 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
