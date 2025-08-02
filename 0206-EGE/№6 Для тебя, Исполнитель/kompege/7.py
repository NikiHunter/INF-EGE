from turtle import *


tracer(0)
screensize(5000, 5000)
m = 50

for _ in range(8):
    for _ in range(4):
        fd(5 * m)
        rt(30)
        fd(6 * m)
        rt(150)
    rt(60)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
