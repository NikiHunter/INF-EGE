from turtle import *


tracer(0)
screensize(5000, 5000)
m = 20

for _ in range(2):
    fd(21 * m)
    rt(90)
    fd(27 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for _ in range(2):
    fd(86 * m)
    rt(90)
    fd(47 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()
print(18 * 13)
mainloop()
