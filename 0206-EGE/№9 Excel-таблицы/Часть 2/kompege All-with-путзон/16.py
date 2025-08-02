with open("9_8609.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k, g = sorted(i)
    no_pos = [x for x in i if i.count(x) == 1]
    if len(no_pos) == 5:
        if 2 * (g + m) <= 3 * (n + p + k):  # ЧИТАТЬ ВНИМАТЕЛЬНО; ПИСАТЬ РАЗМЕРЕННО-СВЕРЯЮЩЕ-ВНИМАТЕЛЬНО!!!!
            count += 1
print(count)
