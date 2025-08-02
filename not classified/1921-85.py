def f(s, m, all_or_any=all, check_for_existance_of_lose=False):
    # print(s, m)
    if s == 1: return m % 2 == 0
    if m == 0: return 0
    fn = [f(s - 2 if s % 2 else s // 2, m - 1), (0 if s % 3 and s < 3 else f(s - 3 if s % 3 else s // 3, m - 1))]
    if check_for_existance_of_lose:
        return (False in fn and True in fn)
    return any(fn) if (m - 1) % 2 == 0 else all_or_any(fn)


print("19)", [i for i in range(2, 38) if f(i, 1) and f(i, 2, any)])
print("20)", [i for i in range(2, 38) if not f(i, 1) and f(i, 3)])
print("21)", [i for i in range(2, 38) if f(i, 2, any, check_for_existance_of_lose=True)])
