def f(s, k, m):
    if s + k >= 30:
        return m % 2 == 0
    if m == 0:
        return 0

    main_g = [f(s + 1, k, m - 1), f(s, k + 1, m - 1), f(s * 2, k, m - 1), f(s, k * 2, m - 1)]
    return any(main_g) if (m - 1) % 2 == 0 else all(main_g)


print("#19", len([sorted((s1, s2)) for s1 in range(1, 30) for s2 in range(1, 30) if f(s1, s2, 2) and (s1 + s2) < 30]))
