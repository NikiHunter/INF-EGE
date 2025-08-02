with open("17.txt") as f:
    f = f.readlines()


res = []
for i in range(len(f) - 1):
    m, n = int(f[i]), int(f[i + 1])
    if (m % 3 == 0 or n % 3 == 0) and (m + n) % 5 == 0:
        res.append(m + n)
print(len(res), max(res))
