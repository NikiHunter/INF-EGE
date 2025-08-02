from turtle import *


tracer(0)
screensize(5000, 5000)
m = 20

for _ in range(3):
    down()
    for _ in range(2):
        fd(7 * m)
        rt(90)
        fd(7 * m)
        rt(90)
    up()
    fd(6 * m)
    rt(90)
    fd(6 * m)
    lt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
