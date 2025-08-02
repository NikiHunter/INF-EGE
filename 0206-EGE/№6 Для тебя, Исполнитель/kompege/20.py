from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30


for _ in range(2):
    goto(xcor() + 6 * m, ycor() + 2 * m)
    goto(xcor() + 0 * m, ycor() + -2 * m)

for _ in range(3):
    goto(xcor() + 2 * m, ycor() + -1 * m)
    goto(xcor() + -2 * m, ycor() + -1 * m)

for _ in range(6):
    goto(xcor() + -2 * m, ycor() + 1 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()