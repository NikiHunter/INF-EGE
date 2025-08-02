def f(x, y, a):
    return (x > a) or (y > x) or (2*y + x < 110)


for a_ in range(200, 1, -1):
    if all(f(x_, y_, a_) for x_ in range(0, 1000) for y_ in range(0, 1000)):
        print(a_)
        break
