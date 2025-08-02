from turtle import *


tracer(0)
screensize(5000, 5000)
m = 50
for _ in range(4):
    forward(12 * m)
    right(90)
right(30)
for _ in range(3):
    forward(8 * m)
    right(60)
    forward(8 * m)
    right(120)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
print(11 * 11 - 9)
mainloop()
