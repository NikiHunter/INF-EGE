from turtle import *


tracer(0)
screensize(5000, 5000)
m = 20

for _ in range(2):
    fd(24 * m)
    rt(90)
    fd(10 * m)
    rt(90)
fd(3 * m)
lt(90)
fd(13 * m)
rt(90)
for _ in range(2):
    fd(9 * m)
    rt(90)
    fd(32 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
