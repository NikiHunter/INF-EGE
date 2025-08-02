from turtle import *

k = 10
tracer(0)
screensize(20_000, 20_000)

color('blue', 'red')

begin_fill()

for _ in range(4):
    fd(10 * k)
    lt(90)

end_fill()
up()

fd(3 * k)
rt(270)
fd(5 * k)
rt(90)

down()
begin_fill()

for _ in range(2):
    fd(10 * k)
    rt(270)
    fd(12 * k)
    rt(270)

end_fill()
up()
update()

canvas = getcanvas()
c = 0

for x in range(-300, 300):
    for y in range(-300, 300):
        p = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        colors = [canvas.itemcget(e, 'fill') for e in p]
        if len(p) > 0 and 'red' in colors or 'blue' in colors:
            c += 1
            goto(x * k, -y * k)
            dot(4, 'green')
print(c)
done()
