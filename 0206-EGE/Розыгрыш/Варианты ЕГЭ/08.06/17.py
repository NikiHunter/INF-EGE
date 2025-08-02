with open("demo_2025_17.txt") as f:
    f = [int(i) for i in f.readlines()]

min_f = min(f)
count, max_par = 0, 0
for i in range(len(f) - 1):
    m, n = f[i], f[i + 1]
    if m % 16 == min_f or n % 16 == min_f:
        count += 1
        max_par = (m + n) if (m + n) > max_par else max_par
print(count, max_par)
