with open("9_2929.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p = max(i), sum(i) - max(i) - min(i), min(i)
    if (m + p) / 2 <= n:
        count += 1
print(count)
