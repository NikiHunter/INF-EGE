def f(c, e):
    if c > e or c in [15]:
        return 0
    if c == e:
        return 1
    return f(c + 1, e) + f(c * 2, e)


print(f(1, 10) * f(10, 22))
