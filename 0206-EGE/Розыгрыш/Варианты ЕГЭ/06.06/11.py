with open("17.txt") as f:
    f = [int(i) for i in f.readlines()]


min_xx = min([x for x in f if len(str(x)) >= 2 and str(x)[-1] == str(x)[-2]]) ** 2
count = 0
max_c = 0
for i in range(len(f) - 1):
    m, n = f[i], f[i + 1]
    if (len(str(n)) >= 2 and str(m)[-1] == str(n)[-2]) or (len(str(m)) >= 2 and str(m)[-2] == str(n)[-1]):
        if (n % 7 == 0 and m % 7 != 0) or (m % 7 == 0 and n % 7 != 0):
            if (m ** 2 + n ** 2) <= min_xx:
                count += 1
                max_c = (m ** 2 + n ** 2) if (m ** 2 + n ** 2) > max_c else max_c
print(count, max_c)
