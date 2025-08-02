with open("9_2097.txt") as f:
    f = [list(map(int, i.strip().split("\t"))) for i in f.readlines()]


count = 0
for i in range(len(f)):
    x0, y0, x1, y1 = f[i]
    if (min(x1, x0) <= 0 <= max(x1, x0) and ((y0 > 0 and y1 > 0) or (y0 < 0 and y1 < 0))) or \
            (min(y0, y1) <= 0 <= max(y0, y1) and ((x0 > 0 and x1 > 0) or (x0 < 0 and x1 < 0))):
        count += 1
    elif (y0 * y1 > 0 and x1 * x0 <= 0) or (y0 * y1 <= 0 and x1 * x0 > 0):  # other way to write
        count += 1
print(count)
