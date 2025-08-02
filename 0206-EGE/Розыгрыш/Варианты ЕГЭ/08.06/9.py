with open("9.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]

count = 0
for i in f:
    m, n, p, g, h, j = i
    pos = [x for x in i if i.count(x) == 3]
    no_pos = [x for x in i if i.count(x) == 1]
    if (len(pos) == 3 == len(no_pos)) and (pos[0] >= (sum(no_pos) / len(no_pos))):
        count += 1
print(count)
