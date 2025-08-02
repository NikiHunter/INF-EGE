from turtle import *


tracer(0)
screensize(5000, 5000)
m = 50

for _ in range(14):
    for _ in range(3):
        fd(3 * m)
        rt(90)
    lt(180)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
