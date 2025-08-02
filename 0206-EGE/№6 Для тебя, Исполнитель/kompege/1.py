from turtle import *


tracer(0)
screensize(5000, 5000)
m = 30

for _ in range(45):
    fd(10 * m)
    rt(8)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "violet")
update()

for n in range(3, 100):
    if (n - 2) * 180 / n == (180 - 8):
        print(n)
        break
mainloop()
