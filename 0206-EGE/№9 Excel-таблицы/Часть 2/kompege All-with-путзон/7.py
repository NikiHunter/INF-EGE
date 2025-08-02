with open("9_4634.txt") as f:
    f = [list(map(int, i.split())) for i in f]


count = 0
for i in f:
    m, n, p, k = sorted(i)
    if (m * n == p * k) or (m * p == n * k) or (m * k == n * p):
        if p ** 2 > (m * k):
            count += 1
print(count)
