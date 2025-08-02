from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30

for _ in range(3):
    goto(xcor() + -3 * m, ycor() + -4 * m)
    goto(xcor() + -12 * m, ycor() + -5 * m)
    goto(xcor() + 0, ycor() + 1 * m)
    goto(xcor() + 15 * m, ycor() + 8 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
