from turtle import *


tracer(0)
screensize(5000, 5000)
m = 80

for _ in range(16):
    lt(36)
    fd(4 * m)
    lt(36)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(5, "violet")
update()
mainloop()
