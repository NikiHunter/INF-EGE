with open("9_4669.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    max_min, p = max(i) + min(i), sum(i) - max(i) - min(i)
    if max_min < p:
        count += 1
print(count)
