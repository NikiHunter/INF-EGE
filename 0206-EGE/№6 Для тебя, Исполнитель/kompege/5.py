from turtle import *


tracer(0)
screensize(5000, 5000)
m = 60

fd(9 * m)
rt(90)
for _ in range(2):
    fd(3 * m)
    rt(90)
    fd(3 * m)
    rt(270)

for _ in range(2):
    fd(3 * m)
    rt(90)
fd(9 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
