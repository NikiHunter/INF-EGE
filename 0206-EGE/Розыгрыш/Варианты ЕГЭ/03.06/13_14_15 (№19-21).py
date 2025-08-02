def fn(a, m, all_or_any=all):
    if a >= 70:
        return m % 2 == 0
    if m == 0:
        return 0
    fm = [fn(a + 1, m - 1), fn(a + 4, m - 1), fn(a * 5, m - 1)]
    return any(fm) if (m - 1) % 2 == 0 else all_or_any(fm)


print("19.", min([s for s in range(1, 70) if fn(s, 2, all_or_any=any)]))
print("20.", [s for s in range(1, 70) if not fn(s, 1) and fn(s, 3)])
print("21.", [s for s in range(1, 70) if not fn(s, 2) and fn(s, 4)])
