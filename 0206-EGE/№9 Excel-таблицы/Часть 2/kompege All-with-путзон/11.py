with open("9_5126.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]

count = 0
for i in f:
    pos = [x for x in i if i.count(x) == 3]
    no_pos = [x for x in i if i.count(x) == 1]
    if len(pos) == len(no_pos) == 3:
        if sum(no_pos) / 3 <= sum(pos):
            count += 1
    elif len(pos) == len(no_pos):  # CHECK THE LEN ALWAYS
        ...
        # print(pos, no_pos)
print(count)
