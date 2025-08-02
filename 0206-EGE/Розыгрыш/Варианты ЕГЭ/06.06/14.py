def f(c, e):
    if c < e or c in [20]:
        return 0
    if c == e:
        return 1
    return f(c - 2, e) + f(c // 2, e)


print(f(80, 40) * f(40, 1))
