def f(s, m, all_or_any=all):
    if s <= 21:
        return m % 2 == 0
    if m == 0:
        return 0

    move_g = [f(s - 3, m - 1), f(s - 7, m - 1), f(s // 4, m - 1)]

    return any(move_g) if (m - 1) % 2 == 0 else all_or_any(move_g)


print("#19", [k for k in range(22, 100) if f(k, 2) and not f(k, 1)])
print("#20", [k for k in range(22, 100) if f(k, 3) and not f(k, 1)])
print("#21", [k for k in range(22, 100) if f(k, 4) and not f(k, 2)])
