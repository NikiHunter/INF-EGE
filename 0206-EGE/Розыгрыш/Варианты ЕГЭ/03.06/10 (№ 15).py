def f(x, a):
    return ((x & 25) != 0) <= (((x & 19) == 0) <= ((x & a) != 0))


for a_ in range(1, 1000):
    if all(f(x_, a_) for x_ in range(1, 10000)):
        print(a_)
        break
