""" №19-1135 """


def fn(a, b, c, m):
    if a + b + c >= 73:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a + 3, b, c, m - 1), fn(a, b + 3, c, m - 1), fn(a, b, c + 3, m - 1),
          fn(a + 13, b, c, m - 1), fn(a, b + 13, c, m - 1), fn(a, b, c + 13, m - 1),
          fn(a + 23, b, c, m - 1), fn(a, b + 23, c, m - 1), fn(a, b, c + 23, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all(fm)


print("19.", [s for s in range(1, 24) if fn(2, s, s * 2, 2)])  # all -> any
print("20.", [s for s in range(1, 60) if not fn(2, s, s * 2, 1) and fn(2, s, s * 2, 3)])  # min and max of list
print("21.", [s for s in range(1, 60) if not fn(2, s, s * 2, 2) and fn(2, s, s * 2, 4)])  # 2 maximums
