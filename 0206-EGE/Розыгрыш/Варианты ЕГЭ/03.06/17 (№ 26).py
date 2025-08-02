with open("28140.txt") as f:
    f = f.readlines()

m, n = map(int, f[0].split(" "))
all_archives = []
for i in range(n):
    all_archives.append(int(f[i + 1]))
mmr_left, count = 0, 0
for ind, arc in enumerate(sorted(all_archives)):
    if mmr_left + arc > m:
        print(count, sorted(all_archives)[ind - 1])
        break
    mmr_left += arc
    count += 1
