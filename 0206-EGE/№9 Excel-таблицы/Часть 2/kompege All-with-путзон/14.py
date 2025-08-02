with open("9_9778.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


for num_ind, i in enumerate(f):
    m, n, p, k, g, h = sorted(i)
    pos = [x for x in i if i.count(x) == 2]
    no_pos = [x for x in i if i.count(x) == 1]
    # ЧИТАТЬ УСЛОВИЕ ПОЛНОСТЬЮ!!! ВНИМАТЕЛЬНО!!! ПОЛНОСТЬЮ!!!
    if len(pos) == 2 and len(no_pos) == 4:
        if pos[0] >= sum(no_pos) / 4:
            print(num_ind + 1)
            break
