with open("9_6999.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, g, h, j = sorted(i)
    krat_3 = [x for x in i if x % 3 == 0]
    if len(krat_3) == 3:
        if j - m <= sum(krat_3):
            count += 1
print(count)
