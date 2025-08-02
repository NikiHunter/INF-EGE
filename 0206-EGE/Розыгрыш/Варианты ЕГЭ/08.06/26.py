with open("26_1.txt") as f:
    inp = []
    for _ in range(int(next(f))):
        inp.append(list(map(int, next(f).split())))
    inp = sorted(inp, key=lambda x: x[1] + x[2] + x[3] + x[4], reverse=True)

ans, not_ans = [], []
for i in inp:
    if len(ans) == len(inp) / 4:
        print((ans + not_ans)[2497], (ans + not_ans)[2498])
    if 2 not in i:
        ans.append(i)
    else:
        not_ans.append(i)
# 26 поспидранить!!!!!
