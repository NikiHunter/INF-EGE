with open("1_17.txt") as f:
    f = f.readlines()

max_17 = max([int(i) for i in f if i.strip()[-2:] == "17"])
count = 0
for i in range(len(f) - 2):
    m, n, p = f[i].strip(), f[i + 1].strip(), f[i + 2].strip()
    if ((len(m) == 3 and len(n) != 3 and len(p) != 3) or
            (len(m) != 3 and len(n) != 3 and len(p) == 3) or (len(m) != 3 and len(n) == 3 and len(p) != 3)) and \
            sum(map(int, (m, n, p))) < max_17:
        count += 1
print(count)
