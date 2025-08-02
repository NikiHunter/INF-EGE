with open("9_5284.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k, g, h = sorted(i)
    # РАБОТАЕТ ХОТЯ БЫ ОДНО ИЗ УСЛОВИЙ!!!; ЧИТАТЬ ВНИМАТЕЛЬНЕЕЕЕЕЕ
    if (m + h) ** 2 > (n ** 2 + p ** 2 + k ** 2 + g ** 2):  # БОЛЬШЕ СУММЫ КВАДРАТОВ
        count += 1
    else:
        pos = [x for x in i if i.count(x) == 3]
        no_pos = [x for x in i if i.count(x) == 1]
        if len(no_pos) == len(pos) == 3:
            count += 1
print(count)
