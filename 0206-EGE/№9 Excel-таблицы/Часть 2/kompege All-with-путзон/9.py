with open("9_4637.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k = sorted(i)
    if k ** 3 >= (2 * m * n * p):
        if m > 10 and n > 10 and p > 10 and k > 10:
            count += 1
print(count)
