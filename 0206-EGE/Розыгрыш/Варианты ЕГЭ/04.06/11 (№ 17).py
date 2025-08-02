with open("17.txt") as f:
    f = [i.strip() for i in f.readlines()]

min_sq_3 = min([int(i) for i in f if i[-1] == "3"]) ** 2  # негативные числа
res = []
for i in range(len(f) - 1):
    m, n = int(f[i]), int(f[i + 1])
    if f[i][-1] == f[i + 1][-1] and (((m % 3 == 0) and (n % 3 != 0)) or
                                     ((m % 3 != 0) and (n % 3 == 0))) \
            and (m ** 2 + n ** 2) <= min_sq_3:
        res.append((m ** 2 + n ** 2))
print(len(res), max(res))
