from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30

for _ in range(10):  # СМЕЩЕНИЕ НА ВЕКТОР; ЛУЧШЕ В КУМИРЕ ДЕЛАТЬ
    goto(xcor() + 3 * m, ycor() + 6 * m)
    goto(xcor() + 7 * m, ycor() + -2 * m)
    goto(xcor() + -10 * m, ycor() + -4 * m)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
mainloop()
