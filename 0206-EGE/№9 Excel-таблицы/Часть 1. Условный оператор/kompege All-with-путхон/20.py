from math import dist


with open("9_2104.txt") as f:
    f = [list(map(int, i.strip().split())) for i in f.readlines()]

count = 0
for i in f:
    x0, y0, x1, y1 = i
    if (x0 * x1 < 0 or y0 * y1 < 0) and dist((x0, y0), (x1, y1)) <= 5:
        count += 1
print(count)
