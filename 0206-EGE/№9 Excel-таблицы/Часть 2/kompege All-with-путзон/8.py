with open("9_4636.txt") as f:
    f = [list(map(int, i.split())) for i in f]


count = 0
for i in f:
    m, n, p, k = sorted(i)
    if k - m >= 50:
        if n * p <= 1000:
            count += 1
print(count)
