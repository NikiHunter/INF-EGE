""" №19-2370 """


def fn(a, m):
    if a >= 2163:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a + 1, m - 1), fn(a * 3, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all(fm)


print("19.", [s for s in range(1, 2163) if fn(s, 2)])
print("20.", [s for s in range(1, 2163) if not fn(s, 1) and fn(s, 3)])
print("21.", min([s for s in range(1, 2163) if not fn(s, 2) and fn(s, 4)]))
