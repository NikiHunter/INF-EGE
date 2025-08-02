with open("9_6925.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, g, h, j = sorted(i)
    pos = [x for x in i if i.count(x) == 2]
    no_pos = [x for x in i if i.count(x) == 1]
    sr_chot = [x for x in i if x % 2 == 0]
    sr_chot = sr_chot if len(sr_chot) else [0]
    sr_no_chot = [x for x in i if x % 2]
    sr_no_chot = sr_no_chot if len(sr_no_chot) else [0]
    # ТОЛЬКО ОДНО ИЗ УСЛОВИЙ!!!! ЧИТАТЬ ВНИМАТЕЛЬНО!!!!! ТОЛЬКО!!!! ИЛИ ХОТЯ БЫ !!!!!
    type_true = 0
    if len(pos) == 2 and len(no_pos) == 4:
        type_true += 1
    if abs(sum(sr_chot) / len(sr_chot) - sum(sr_no_chot) / len(sr_no_chot)) > 50:
        type_true += 1
    if type_true == 1:
        count += 1
print(count)
