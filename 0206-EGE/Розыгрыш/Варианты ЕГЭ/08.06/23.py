def calc(m, n):
    if m < n:
        return 0
    if m == n:
        return 1
    return calc(m - 1, n) + calc(m - 3, n) + calc(m // 2, n)


print(calc(31, 20) * calc(20, 3) + calc(31, 8) * calc(8, 3))
