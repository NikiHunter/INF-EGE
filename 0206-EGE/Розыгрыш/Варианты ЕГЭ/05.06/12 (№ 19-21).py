def f(s, k, m, any_or_all=all):
    if s + k >= 74:
        return m % 2 == 0
    if m == 0:
        return 0

    move_g = [f(s + 1, k, m - 1), f(s * 2, k, m - 1), f(s, k + 1, m - 1), f(s, k * 2, m - 1)]

    return any(move_g) if (m - 1) % 2 == 0 else any_or_all(move_g)


print("#19", min([s2 for s2 in range(1, 62) if f(12, s2, 2, any_or_all=any) and (12 + s2) < 74]))
print("#20", "".join(map(str, [s2 for s2 in range(1, 62) if not f(12, s2, 1) and f(12, s2, 3) and (12 + s2) < 74])))
print("#21", min([s2 for s2 in range(1, 62) if not f(12, s2, 2) and f(12, s2, 4) and (12 + s2) < 74]))
