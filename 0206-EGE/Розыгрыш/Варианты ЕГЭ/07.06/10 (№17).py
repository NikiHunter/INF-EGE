with open("17.txt") as f:
    f = [int(i) for i in f.readlines()]

ans = []
for i in range(len(f)):
    for j in range(i + 1, len(f)):  # ТК ПОРЯДОК НЕ ВАЖЕН; ЗАПОМНИТЬ!!!!
        m, n = f[i], f[j]
        if (m + n) % 2 and (m * n) % 5 == 0:
            ans.append(m + n)
print(len(ans), max(ans))
