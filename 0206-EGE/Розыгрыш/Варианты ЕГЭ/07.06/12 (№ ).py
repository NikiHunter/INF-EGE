def f(s, k, m, any_or_all=all):
    if s + k >= 107:
        return m % 2 == 0
    if m == 0:
        return 0

    move_g = [f(s + 1, k, m - 1), f(s * 2, k, m - 1),
              f(s, k + 1, m - 1), f(s, k * 2, m - 1)]

    return any(move_g) if (m - 1) % 2 == 0 else any_or_all(move_g)


print("#19", [s2 for s2 in range(1, 94) if f(13, s2, 2, any_or_all=any)])
print("#20 ", *[s2 for s2 in range(1, 94) if not f(13, s2, 1) and f(13, s2, 3)], sep="")
print("#21 ", [s2 for s2 in range(1, 94) if not f(13, s2, 2) and f(13, s2, 4) and f(13, s2, 2, any_or_all=any)])
