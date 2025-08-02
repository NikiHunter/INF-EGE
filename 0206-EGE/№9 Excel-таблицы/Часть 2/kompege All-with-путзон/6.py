with open("9_4633.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k = sorted(i)
    if (m + n == p + k) or (m + p == n + k) or (m + k == p + n):
        if (k - m) < ((n + p) - k):
            count += 1
print(count)
