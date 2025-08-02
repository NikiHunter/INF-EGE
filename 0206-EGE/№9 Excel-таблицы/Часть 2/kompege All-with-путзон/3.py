with open("9_3150.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p = sorted(i)
    if p ** 2 > (2 * m * n):
        count += 1
print(count)
