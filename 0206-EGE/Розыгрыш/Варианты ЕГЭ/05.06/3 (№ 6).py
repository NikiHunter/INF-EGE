from turtle import *


tracer(0)
screensize(5000, 5000)
m = 50

right(90)
for _ in range(7):
    right(45)
    fd(11 * m)
    right(45)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, "violet")
update()
print((1 + 3 + 5 + 7 + 9 + 11 + 13) * 2 + 15)  # СЧИТАТЬ В ПУТХОНЕ ТОЛЬКО
mainloop()
