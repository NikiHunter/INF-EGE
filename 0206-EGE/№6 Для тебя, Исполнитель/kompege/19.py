from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30


for _ in range(5):
    goto(xcor() + 5 * m, ycor() + 4 * m)
    goto(xcor() + 4 * m, ycor() + -4 * m)
    goto(xcor() + -7 * m, ycor() + -2 * m)
    goto(xcor() + -2 * m, ycor() + 2 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
