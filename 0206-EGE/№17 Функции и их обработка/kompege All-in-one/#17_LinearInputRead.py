def task11():
    with open("17_2002.txt") as f:
        f = f.readlines()
    ans = []
    for i in range(len(f) - 3):
        a, b, c, d = map(int, (f[i], f[i + 1], f[i + 2], f[i + 3]))
        if a >= b >= c >= d and max([a, b, c, d]) - min([a, b, c, d]) > 1000:
            ans.append(sum([a, b, c, d]))
    return len(ans), min(ans)


def task12():
    with open("17_2400.txt") as f:
        f = f.readlines()
    ans = []
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if a + b >= 100 and (abs(a) != a or abs(b) != b):
            ans.append(a * b)
    return len(ans), max(ans)


def task13():
    with open("17_2401.txt") as f:
        f = f.readlines()
    ans = []
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if 50 <= (abs(a) + abs(b)) <= 200:
            ans.append(a)
            ans.append(b)
    return len(ans) // 2, min(ans)


def task14():
    with open("17_2238.txt") as f:
        f = f.readlines()
    ans, min_ar = [], sum([int(i) for i in f]) / len(f)
    for i in range(len(f) - 2):
        a, b, c = int(f[i]), int(f[i + 1]), int(f[i + 2])
        if (a > min_ar) + (b > min_ar) + (c > min_ar) >= 2:
            ans.append(sum([a, b, c]))
    return len(ans), max(ans)


def task15():
    with open("17_2239.txt") as f:
        f = f.readlines()
    ans, max_19 = [], max([int(i) for i in f if int(i) % 19 == 0])
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if (a > max_19) or b > max_19:
            ans.append(a + b)
    return len(ans), min(ans)


def task16():
    with open("17_2309.txt") as f:
        f = f.readlines()
    ans_11, ans_17 = [], []
    for i in f:
        if int(i) % 11 == 0:
            ans_11.append(int(i))
        if int(i) % 17 == 0:
            ans_17.append(int(i))
    return (len(ans_11), min(ans_11)) if len(ans_11) > len(ans_17) else (len(ans_17), max(ans_17))


def task17():
    with open("17_2310.txt") as f:
        f = f.readlines()
    ans, ends_in_4 = [], [int(i) for i in f if i.strip()[-1] == "4"]
    sum_min_max_4 = min(ends_in_4) + max(ends_in_4)
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if a + b < sum_min_max_4:
            ans.append(a + b)
    return len(ans), max(ans)


def int_to_8(num: int) -> str:
    tmp_str = ""
    while num > 0:
        tmp_str += str(num % 8)
        num //= 8
    return tmp_str[::-1]


def task18():
    with open("17_2403.txt") as f:
        f = f.readlines()
    ans = []
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if ((a % 9 == 0 and int_to_8(abs(b))[-1] == "3" and b % 9 != 0) or  # noqa РОВНО ОДНО ЧИСЛО; ЧИТАТЬ ВНИМАТЕЛЬНО УСЛОВИЕ
                (b % 9 == 0 and int_to_8(abs(a))[-1] == "3" and a % 9 != 0)):
            ans.append(max(a, b))
    return len(ans), max(ans)


def task19():  # ТОЛЬКО; ОДНО; ЕДИНСТВЕННОЕ - ключевые слова
    with open("17_2398.txt") as f:
        f = f.readlines()
    ans = []
    for i in range(len(f) - 2):
        a, b, c = int(f[i]), int(f[i + 1]), int(f[i + 2])
        if (abs(b) == b and str(b)[-1] == "9" and not(abs(c) == c and str(c)[-1] == "9") and
                not(abs(a) == a and str(a)[-1] == "9")):
            ans.append(a + b + c)
    return len(ans), max(ans)


def task20():
    with open("17_2399.txt") as f:
        f = f.readlines()
    ans = []
    sum_digits_35 = sum([sum(int(x) for x in i.strip()) for i in f if int(i) % 35 == 0])
    for i in range(len(f) - 1):
        a, b = int(f[i]), int(f[i + 1])
        if ((a > sum_digits_35 >= b and hex(b)[-2:].upper() == "EF") or  # noqa ТОЛЬКО; ОДНО; ЕДИНСТВЕННОЕ - ключевые слова
                (b > sum_digits_35 >= a and hex(a)[-2:].upper() == "EF")):
            ans.append(a + b)
    return len(ans), min(ans)


if __name__ == "__main__":
    print("#11", *task11())
    print("#12", *task12())
    print("#13", *task13())
    print("#14", *task14())
    print("#15", *task15())
    print("#16", *task16())
    print("#17", *task17())
    print("#18", *task18())
    print("#19", *task19())
    print("#20", *task20())
