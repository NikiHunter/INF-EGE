from turtle import *


tracer(0)
screensize(5000, 5000)
m = 40

for _ in range(15):
    fd(7 * m)
    rt(30)
    fd(8 * m)
    rt(150)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
