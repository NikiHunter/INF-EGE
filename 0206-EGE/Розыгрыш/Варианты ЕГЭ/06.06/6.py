with open("9.txt") as f:
    f = [list(map(int, i.strip().split())) for i in f.readlines()]


count = 0
for i in range(len(f)):
    ind_c = sum([g for g in f[i] if f[i].count(g) == 3]) ** 2
    ind_n = sum([n for n in f[i] if f[i].count(n) == 1]) ** 2
    if sum([f[i].count(count) for count in f[i]]) == sum([3, 3, 3, 1, 1, 1]) and ind_c > ind_n:
        count += 1
print(count)
