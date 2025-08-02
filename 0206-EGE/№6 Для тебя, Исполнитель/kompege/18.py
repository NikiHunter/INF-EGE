from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30


for _ in range(5):
    goto(xcor() + 6 * m, ycor() + 8 * m)
    goto(xcor() + -8 * m, ycor() + 4 * m)
    goto(xcor() + 2 * m, ycor() + -12 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
print(int(148 ** 0.5 + 10 + 80 ** 0.5))
mainloop()
