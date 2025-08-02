""" №19-1135 """


def fn(a, b, m):
    if a + b >= 68:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a + 1, b, m - 1), fn(a + b, b, m - 1), fn(a, b + 1, m - 1), fn(a, b + a, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all(fm)


print("19.", [s for s in range(1, 60) if fn(8, s, 2)])  # all -> any
print("20.", [s for s in range(1, 60) if not fn(8, s, 1) and fn(8, s, 3)])
print("21.", min([s for s in range(1, 60) if not fn(8, s, 2) and fn(8, s, 4)]))
