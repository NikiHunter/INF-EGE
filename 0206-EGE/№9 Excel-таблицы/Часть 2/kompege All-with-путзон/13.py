with open("9_9740.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k, g, h, j = sorted(i)
    pos = [x for x in i if i.count(x) == 3]
    no_pos = [x for x in i if i.count(x) == 1]
    if len(pos) == 3 and len(no_pos) == 4:
        if sum(no_pos) / 4 <= pos[0]:
            count += 1
print(count)
