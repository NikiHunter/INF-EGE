with open("9_9832.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


for i in f:
    m, n, p, k, g, h, j = sorted(i)
    pos = [x for x in i if i.count(x) == 2]
    no_pos = [x for x in i if i.count(x) == 1]
    if len(pos) == 4 and len(no_pos) == 3:
        if i.count(j) == 1:
            sum_nums = sum(i)
            print(sum_nums)
            break  # 261!!!!!! goreosddrgfjdgfopjtfenjlgfvjb dfijojskmjg
