with open("9_6357.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, g, h, j = sorted(i)
    pos = [x for x in i if i.count(x) != 1]
    no_pos = [x for x in i if i.count(x) == 1]
    if len(pos) > 0 and len(no_pos) > 0:
        if sum(no_pos) / len(no_pos) < sum(pos) / len(pos):
            count += 1
print(count)
