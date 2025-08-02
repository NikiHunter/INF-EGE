""" №19-843 """


def fn(a, b, m):
    if a + b <= 20:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a - 1, b, m - 1), fn((a + 1) // 2, b, m - 1), fn(a, b - 1, m - 1), fn(a, (b + 1) // 2, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all(fm)


print("19.", [s for s in range(11, 1000) if fn(10, s, 2)])
print("20.", [s for s in range(11, 1000) if not fn(10, s, 1) and fn(10, s, 3)])
print("21.", min([s for s in range(11, 1000) if not fn(10, s, 2) and fn(10, s, 4)]))
