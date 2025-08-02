from math import sqrt
from fnmatch import fnmatch


def is_prime(n: int):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def dividers(n: int) -> list[int, ...]:
    div_list = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            div_list.append(i)
    return div_list


def all_div(n: int) -> list[int, ...]:
    div_list = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            div_list.append(i)
            div_list.append(n // i)
    return div_list


def task16():
    ans = []
    for i in range(125697, 125721 + 1):
        div_tmp = dividers(i)
        div_prime = [x for x in div_tmp if is_prime(x) and i / x == int(i / x) and is_prime(i // x)]
        for u in range(len(div_prime)):
            ans.append((min(div_prime[u], i // div_prime[u]), max(div_prime[u], i // div_prime[u])))
    return [" ".join(map(str, m)) for m in ans]


def task17():
    ans = []
    for i in range(106732567, 152673836 + 1):  # p**x1 * p**x2 * p**x3 = i; (x1 + 1)(x2 + 1)(x3 + 1) == 5 count dividers
        if not sqrt(i) == int(sqrt(i)):  # from 102 to 111 + 1; check for p ** 4?
            continue
        div_tmp = dividers(i)
        if len(div_tmp) == 2:
            ans.append((i, i // div_tmp[0]))  # max is i / min found div
        if len(ans) == 10:
            break
    return [" ".join(map(str, m)) for m in ans]


def task18():
    ans = []
    for i in range(55_000_000, 60_000_000 + 1):
        tmp_i = i
        while tmp_i % 2 == 0:
            tmp_i //= 2
        if int(tmp_i ** 0.25) ** 4 == tmp_i and is_prime(int(tmp_i ** 0.25)):
            ans.append((i, tmp_i))
    return [" ".join(map(str, m)) for m in ans]


def task19():  # TODO: understand this
    ans = []
    for i in range(113_000_000, 114_000_000 + 1):
        if i % 2 == 0 and i % 4 and int(sqrt(i // 2)) == sqrt(i // 2) and is_prime(int(sqrt(i // 2))):
            ans.append((i, int(sqrt(i // 2)) * 2))
    return [" ".join(map(str, m)) for m in ans]


def task20():
    return [f"{810810000} {int(810810000 / 3 ** 4 / 5 ** 4 / 2 ** 4 / 11 / 7)}"]


def task_s1():
    ans = []
    # TODO: SO SLOW, SO "Va-Bank" Method used
    # for i in range(123_450_600, 1_000_000_000, 17):
    #     if fnmatch(str(i), "12345?6?8") and i % 17 == 0:
    #         ans.append((i, i // 17))
    for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if fnmatch(f"12345{x}6{y}8", "12345*6*8") and int(f"12345{x}6{y}8") % 17 == 0: # noqa idk why fnmatch used....
                ans.append((int(f"12345{x}6{y}8"), int(f"12345{x}6{y}8") // 17))
    return sorted(set([" ".join(map(str, x)) for x in ans]), key=lambda k: int(k.split(" ")[0]))


def task_s2():  # second part' 2-nd task; pls check the video' solve
    ans = []
    for x in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for x1 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for x2 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                for x3 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if int(f"1234{x}{x1}{x2}{x3}7") % 141 == 0 and int(f"1234{x}{x1}{x2}{x3}7") < 10 ** 8:
                        ans.append(" ".join((f"1234{x}{x1}{x2}{x3}7", str(int(f"1234{x}{x1}{x2}{x3}7") // 141))))
    return sorted(set(ans), key=lambda k: int(k.split(" ")[0]))


def task_s3():  # NO fn match
    ans = []
    for x in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for x1 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for x2 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if int(f"123{x}{x1}{x2}567{y}") % 169 == 0 and int(f"123{x}{x1}{x2}567{y}") < 10 ** 9:
                        ans.append(" ".join((f"123{x}{x1}{x2}567{y}", str(int(f"123{x}{x1}{x2}567{y}") // 169))))
    return sorted(set(ans), key=lambda k: int(k.split(" ")[0]))


def task_s4():  # NO FN -> NO EFFECTIVE CUZ MAYBE ERRORS; # TODO: TO FN REWRITE
    ans = []
    for x in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for x1 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for x2 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                for xy in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if int(f"12{x}{x1}45{x2}{xy}") % 51 == 0 and int(f"12{x}{x1}45{x2}{xy}") < 10 ** 6:
                        ans.append(" ".join((f"12{x}{x1}45{x2}{xy}", str(int(f"12{x}{x1}45{x2}{xy}") // 51))))
    return sorted(set(ans), key=lambda k: int(k.split(" ")[0]))


def task_s5():
    ans = []
    for x in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for x1 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            for x2 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                for x3 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    for x4 in ["", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            if int(f"1{y}2139{x}{x1}{x2}{x3}{x4}4") % 2023 == 0 and \
                                    int(f"1{y}2139{x}{x1}{x2}{x3}{x4}4") < 10 ** 10:
                                ans.append(" ".join((f"1{y}2139{x}{x1}{x2}{x3}{x4}4",
                                                     str(int(f"1{y}2139{x}{x1}{x2}{x3}{x4}4") // 2023))))
    return sorted(set(ans), key=lambda k: int(k.split(" ")[0]))


def task_s6():
    ans = []
    for i in range(65_000, 1_000_000):
        if fnmatch(str(i), "6*97*5?") and \
                len(tmp_l := list(filter(lambda x: x % 2 == 0, all_div(i)))) >= 4:
            ans.append(" ".join(map(str, (i, sum(tmp_l)))))
        if len(ans) >= 7:
            break
    return sorted(set(ans), key=lambda k: int(k.split(" ")[0]))


def task_s7():
    ans = []
    for i in range(10_000_000, 90_557, -1):
        if fnmatch(str(i), "9?*55*7"):
            ans.append((i, sum(all_div(i)) % 21))
        if len(ans) >= 5:
            break
    return sorted([" ".join(map(str, x)) for x in ans], key=lambda k: int(k.split(" ")[0]))


def task_s8():
    ans = []
    for i in range(666, 1_000_000):
        if fnmatch(str(i), "?6*6*?6") and i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
            ans.append((i, sum(all_div(i))))
        if len(ans) >= 7:
            break
    return [" ".join(map(str, x)) for x in ans]


def task_s9():
    ans = []
    for i in range(10_000_000, 1, -1):
        if fnmatch(str(i), "14?4*") and i % 217 == 0:
            ans.append((i, sum(filter(lambda k: k % 2, all_div(i)))))
        if len(ans) >= 7:
            break
    return sorted([" ".join(map(str, x)) for x in ans], key=lambda k: int(k.split(" ")[0]))


def task_s10():
    ans = []
    for i in range(700_000, 10_000_000):
        if (fnmatch(str(i), "*0??3*") + fnmatch(str(i), "*4??2") + fnmatch(str(i), "*1*")) == 0 \
                and i % 13 == 0:
            ans.append((i, sum(int(x) for x in str(i))))
        if len(ans) >= 5:
            break
    return [" ".join(map(str, x)) for x in ans]


if __name__ == "__main__":  # TODO: ПЕРЕСМОТРЕТЬ ВИДЕО ПО ЗАДАНИЮ, ОСОБЕННО СЛОЖНЫЕ
    print(dividers(106732610))
    print("#16", *task16(), sep="\n")
    print("#17", *task17(), sep="\n")
    print("#18", *task18(), sep="\n")
    print("#19", *task19(), sep="\n")
    print("#20", *task20(), sep="\n")
    print("#1", *task_s1(), sep="\n")
    print("#2", *task_s2(), sep="\n")
    print("#3", *task_s3(), sep="\n")
    print("#4", *task_s4(), sep="\n")
    print("#5", *task_s5(), sep="\n")
    print("#6", *task_s6(), sep="\n")
    print("#7", *task_s7(), sep="\n")
    print("#8", *task_s8(), sep="\n")
    print("#9", *task_s9(), sep="\n")
    print("#10", *task_s10(), sep="\n")
    print("#")
