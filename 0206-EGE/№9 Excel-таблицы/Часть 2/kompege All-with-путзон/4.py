with open("9_3167.txt") as f:
    f = [list(map(int, i.split())) for i in f.readlines()]


count = 0
for i in f:
    m, n, p, k = sorted(i)
    # СУММА КВАДРАТОВ m ** 2 + n ** 2; КВАДРАТ СУММЫ (m + n) ** 2 СЛЕДИТЬ ЗА КАЖДЫМ
    if (m + k) ** 2 > (n ** 2 + p ** 2):  # ВНИМАНИЕ!!!
        count += 1
print(count)
