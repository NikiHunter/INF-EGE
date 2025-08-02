with open("9_10910.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, g, h, k = sorted(i)
    pos = [x for x in i if i.count(x) != 1]
    if i.count(m) == 1:
        if len(pos) > 0:
            if m + k < sum(pos):
                count += 1
print(count)
