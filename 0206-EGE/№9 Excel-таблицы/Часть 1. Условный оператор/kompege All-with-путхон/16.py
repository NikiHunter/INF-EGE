from math import acos, pi


with open("9_2101.txt") as f:
    f = [list(map(int, i.strip().split())) for i in f.readlines()]


count = 0
print(acos(1/2), pi/3)
for i in range(len(f)):
    m, n, p = f[i]
    if not (m + n > p and m + p > n and n + p > m):
        continue
    """
    или
    m, n, p = sorted(m, n, p)
    if m ** 2 + n ** 2 > p ** 2:
        count += 1
    """
    res1 = acos((n ** 2 + p ** 2 - m ** 2) / (2 * n * p))
    res2 = acos((m ** 2 + p ** 2 - n ** 2) / (2 * m * p))
    res3 = acos((n ** 2 + m ** 2 - p ** 2) / (2 * n * m))
    if res1 < pi / 2 and res2 < pi/2 and res3 < pi/2:
        count += 1
print(count)
