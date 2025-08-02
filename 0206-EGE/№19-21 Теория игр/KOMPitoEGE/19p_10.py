""" №19-853 """


def fn(a, b, m):
    if a + b >= 77:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a + 1, b, m - 1), fn(a * 2, b, m - 1), fn(a, b + 1, m - 1), fn(a, b * 2, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all(fm)


print("19.", (min([s for s in range(1, 70) if fn(7, s, 1)]) + 1) // 2)
print("20.", [s for s in range(1, 70) if not fn(7, s, 1) and fn(7, s, 3)])
print("21.", min([s for s in range(1, 70) if not fn(7, s, 2) and fn(7, s, 4)]))
