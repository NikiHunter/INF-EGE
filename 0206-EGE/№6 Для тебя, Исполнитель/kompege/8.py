from turtle import *


tracer(0)
screensize(5000, 5000)
m = 50

for _ in range(3):
    fd(7 * m)
    rt(90)
fd(8 * m)
for _ in range(3):
    lt(90)
    fd(5 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
