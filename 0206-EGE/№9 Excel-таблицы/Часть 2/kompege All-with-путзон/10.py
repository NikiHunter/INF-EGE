with open("9_4614.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k = sorted(i)
    if k < (m + n + p):
        if sum([i.count(x) for x in i]) == sum([2, 2, 1, 1]):
            count += 1
print(count)
