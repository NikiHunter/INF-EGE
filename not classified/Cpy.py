def f(s, m, all_or_any=all):
    if s >= 151:
        return m % 2 == 0
    if m < 0:
        return 0

    h = set()
    if (s + 1) % 3 != 0:
        h.add(f(s + 1, m - 1))
    if (s + 2) % 3 != 0:
        h.add(f(s + 2, m - 1))
    h.add(f(s * 2, m - 1))
    return any(h) if m % 2 != 0 else all_or_any(h)


print('#19 | ', min([s for s in range(1, 150) if f(s, 2)]))
print('#20 | ', *[s for s in range(1, 150) if f(s, 3) and not f(s, 1)])
print('#21 | ', *[s for s in range(1, 150) if f(s, 4) and not f(s, 2)])
