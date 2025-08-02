""" №19-1202 """


def fn(a, b, m):
    if a + b >= 59:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a + 1, b, m - 1), fn(a * 2, b, m - 1), fn(a, b + 1, m - 1), fn(a, b * 2, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all(fm)


print("19.", min([s for s in range(1, 53) if fn(5, s, 1)]))
print("20.", [s for s in range(1, 53) if not fn(5, s, 1) and fn(5, s, 3)])
print("21.", min([s for s in range(1, 53) if not fn(5, s, 2) and fn(5, s, 4)]))
