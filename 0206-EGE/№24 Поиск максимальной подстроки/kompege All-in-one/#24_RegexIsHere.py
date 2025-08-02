import re


def task1():
    # №1 https://kompege.ru
    with open("24_2420.txt") as f:
        f = f.read()

    matched_str = re.findall(r"([ABEF]*)", f)
    return len(max(matched_str, key=len))


def task2():
    # №2 https://kompege.ru
    with open("24_2426.txt") as f:
        f = f.read()

    matched_str = re.findall(r"(\d*)", f)
    return len(max(matched_str, key=len))


def task3():
    # №3 https://kompege.ru
    with open("24_1040.txt") as f:
        f = f.read()

    matched_str = re.findall(r"(\d*)", f)
    return len(max(matched_str, key=len))


def task4():
    # №4 https://kompege.ru
    with open("24_1428.txt") as f:
        f = f.read()

    matched_str = f.replace("XY", "X Y").replace("XZ", "X Z")  # cuz needed for max string
    return len(max(matched_str.split(" "), key=len))


def task5():
    # №5 https://kompege.ru
    with open("24_1975.txt") as f:
        f = f.read()

    matched_str = f.replace("PP", "P P")  # cuz needed for max string
    return len(max(matched_str.split(" "), key=len))


def task6():
    # №6 https://kompege.ru
    with open("24_1302.txt") as f:
        f = f.read()

    matched_str = f.replace("XZZY", "XZ ZY")  # cuz needed for max string
    return len((max(matched_str.split(" "), key=len))) + 2  # cuz 1 from the left and one from the right symbols


def task7():
    # №7 https://kompege.ru
    with open("24_4627.txt") as f:
        f = f.read()
    # f = f.replace("NPO", "A").replace("PNO", "A")
    # matched_str = re.findall(r"(A*)", f) return len(max(matched_str, key=len))
    matched_str = re.findall(r"(?:NPO|PNO)*", f)
    return len(max(matched_str, key=len)) // 3  # ПОТОМУ ЧТО КОЛИЧЕСТВО ПОСЛЕДОВАТЕЛЬНОСТЕЙ ИЗ 3 СИМВОЛОВ


def task8():
    # №8 https://kompege.ru
    with open("24_4602.txt") as f:
        f = f.read()
    matched_str = re.findall(r"(?:[BCD][AO])*", f)
    return len(max(matched_str, key=len)) // 2  # ПОТОМУ ЧТО ПАРЫ


def task9():
    # №9 https://kompege.ru
    with open("24_4643.txt") as f:
        f = f.read()
    matched_str = re.findall(r"(?:\d\d[AB])*", f)  # [AB] cuz \w - [a-zA-Z0-9]
    return len(max(matched_str, key=len)) // 3  # ПОТОМУ ЧТО КОЛИЧЕСТВО ПОСЛЕДОВАТЕЛЬНОСТЕЙ ИЗ 3 СИМВОЛОВ


def task10():
    # №10 https://kompege.ru
    with open("24_8510.txt") as f:
        f = f.read()
    f = (f.replace("NN", "N N").replace("NP", "N P").replace("PN", "P N")
         .replace("NO", "N O").replace("ON", "O N").replace("OP", "O P")
         .replace("PO", "P O").replace("OO", "O O").replace("PP", "P P"))
    return len(max(f.split(), key=len))


def task11():
    # №11 https://kompege.ru
    with open("24_21.txt") as f:
        f = f.read()
    while ("XX" in f) or ("YY" in f) or ("ZZ" in f):  # Максимум два раза пройдется, однако лучше использовать while
        f = f.replace("XX", "X X").replace("YY", "Y Y").replace("ZZ", "Z Z")  # noqa
    return len(max(f.split(), key=len))  # Лучше всегда выводить сначала строку + ее длину


def task12():
    # №12 https://kompege.ru
    with open("24_2422.txt") as f:
        f = f.read()  # or readline?
    ans = [1] * len(f)
    for i in range(len(f) - 1):  # or just f[i] >= f[i + 1]
        if f[i] == f[i + 1] or (f[i] == "X" and f[i + 1] == "Y") or (f[i] == "Y" and f[i + 1] == "Z") or \
                (f[i] == "X" and f[i + 1] == "Z"):
            ans[i + 1] = ans[i] + 1
    return max(ans)


def task13():
    # №13 https://kompege.ru
    with open("24_2423.txt") as f:
        f = f.read()  # or readline?
    ans = [1] * len(f)
    for i in range(len(f) - 1):
        if f[i] < f[i + 1]:
            ans[i + 1] = ans[i] + 1
    return max(ans)


def task14():
    # №14 https://kompege.ru
    with open("24_2427.txt") as f:
        f = f.read()  # or readline?
    ans = [1] * len(f)
    for i in range(len(f) - 1):
        if ord(f[i]) >= ord(f[i + 1]):
            ans[i + 1] = ans[i] + 1  # лучше всегда перепроверять саму строку
    return f[ans.index(max(ans)) - max(ans) + 1:ans.index(max(ans)) + 1]  # + 1 в начале тк chr("k") < chr("z")


def task15():
    # №15 https://kompege.ru
    with open("24_4113.txt") as f:
        f = f.read()  # or readline?
    while ("BB" in f) or ("DD" in f):
        f = f.replace("BB", ".").replace("DD", ".")
    ans = [1] * len(f)
    for i in range(len(f) - 1):
        if f[i] == ".":  # always check if +1 or -1 of result
            ans[i] = ans[i - 1] + 1
    return max(ans)


def task16():
    # №16 https://kompege.ru
    with open("24_9552.txt") as f:
        orig_f = f = f.read()  # noqa | or readline?
    while ("PC" in f) or ("CSGO" in f):
        f = f.replace("PC", "..").replace("CSGO", "....")  # noqa
    ans = [0] * len(f)  # когда пара - 1, когда количество - 0 (тк лишний символ добавляется)
    for i in range(len(f) - 1):
        if f[i] == ".":  # always check if +1 or -1 of result
            ans[i] = ans[i - 1] + 1
    return max(ans)  # orig_f[ans.index(max(ans)) - max(ans) + 1:ans.index(max(ans)) + 1]


def task17():
    # №17 https://kompege.ru
    with open("24_4546.txt") as f:
        orig_f = f = f.read()  # noqa | or readline?
    # while ("AAA" in f) or ("ABA" in f) or ("ACA" in f) or ("CCC" in f) or ("CAC" in f) or ("CBC" in f):
    #     f = (f.replace("AAA", "...").replace("ABA", "...").replace("ACA", "...")  # noqa
    #          .replace("CAC", "...").replace("CBC", "...").replace("CCC", "..."))
    # ans = [0] * len(f)  # noqa когда пара - 1, когда количество - 0 (тк лишний символ добавляется) - нет, каждый раз лучше проверять строку
    # for i in range(len(f) - 1):
    #     if f[i] == ".":  # always check if +1 or -1 of result
    #         ans[i] = ans[i - 1] + 1
    # return len(orig_f[ans.index(max(ans)) - max(ans) + 1:ans.index(max(ans)) + 1]) / 3

    # ВЕРНОЕ РЕШЕНИЕ
    ans = [0] * len(f)
    for i in range(2, len(f)):
        if f[i] == f[i - 2] == "A" or f[i] == f[i - 2] == "C":
            ans[i] = ans[i - 3] + 1
    return max(ans)


def task18():
    file = open("24_2251.txt")  # without with method? and close cuz' executable after
    f = file.read()  # Задача с динамическим программированием...
    file.close()
    left_d, dynamic_ans, count_d = 0, 0, 0
    for right_d in range(len(f)):
        if f[right_d] == "D":
            count_d += 1
        while count_d > 2:
            if f[left_d] == "D":
                count_d -= 1
            left_d += 1
        if right_d - left_d + 1 > dynamic_ans:
            dynamic_ans = right_d - left_d + 1
    return dynamic_ans


def task19():
    file = open("24_10105.txt")
    f = file.read()
    file.close()
    left_border, dynamic_ans, count_t = 0, 0, 0
    for right_border in range(len(f)):
        if f[right_border] == "T":
            count_t += 1
        while count_t > 100:
            if f[left_border] == "T":
                count_t -= 1
            left_border += 1
        if right_border - left_border + 1 > dynamic_ans:
            dynamic_ans = right_border - left_border + 1
    return dynamic_ans


def task20():
    file = open("24_13715.txt")
    f = file.read()
    file.close()
    left_border, dynamic_ans, count_ab = 0, 0, 0
    for right_border in range(1, len(f)):
        if f[right_border - 1] + f[right_border] == "AB":  # cuz from right to left watching
            count_ab += 1
        while count_ab > 50:
            if f[left_border] + f[left_border + 1] == "AB":
                count_ab -= 1
            left_border += 1
        if count_ab == 50 and (right_border - left_border + 1) > dynamic_ans:
            dynamic_ans = right_border - left_border + 1
    return dynamic_ans


def task21():
    with open("24_12476.txt") as f:
        f = f.read()
    left_border, dynamic_ans, count_ro = 0, 0, 0
    for right_border in range(len(f)):
        if right_border > 1 and (f[right_border - 2] + f[right_border - 1] + f[right_border] == "ROR" or
                                 f[right_border - 2] + f[right_border - 1] + f[right_border] == "ORO"):
            count_ro = 0
            left_border = right_border - 1
        if f[right_border - 1] + f[right_border] == "RO":
            count_ro += 1
        while count_ro == 21:
            dynamic_ans = max(right_border - left_border + 1, dynamic_ans)
            if f[left_border] + f[left_border + 1] == "RO":
                count_ro -= 1
            left_border += 1
    return dynamic_ans


def task22():
    with open("24_6734.txt") as f:
        f = f.read()
    left_border, dynamic_ans, count_dot = 0, float("inf"), 0
    for right_border in range(len(f)):
        if f[right_border] == ".":
            count_dot += 1
        while count_dot == 7:  # для минимума другой способ применяем; применим для максимума?
            dynamic_ans = min(right_border - left_border + 1, dynamic_ans)
            if f[left_border] == ".":
                count_dot -= 1
            left_border += 1
    return dynamic_ans


def task23():
    with open("24_11954.txt") as f:
        f = f.read()
    left_border, dynamic_ans, count_x = 0, float("inf"), 0
    for right_border in range(len(f)):
        if f[right_border] == "Y":
            count_x = 0
            left_border = right_border
        if f[right_border] == "X":
            count_x += 1
        while count_x >= 500:
            dynamic_ans = min(right_border - left_border + 1, dynamic_ans)
            if f[left_border] == "X":
                count_x -= 1
            left_border += 1
    return dynamic_ans


def task24():
    with open("24_9169.txt") as f:
        f = f.read()
    left_border, dynamic_ans, count_bad_fat = 0, float("inf"), 0
    for right_border in range(2, len(f)):
        if (f[right_border - 2] + f[right_border - 1] + f[right_border] == "BAD" or
                f[right_border - 2] + f[right_border - 1] + f[right_border] == "FAT"):
            count_bad_fat += 1
        while count_bad_fat == 3:
            dynamic_ans = min(right_border - left_border + 1, dynamic_ans)
            if (f[left_border] + f[left_border + 1] + f[left_border + 2] == "BAD" or
                    f[left_border] + f[left_border + 1] + f[left_border + 2] == "FAT"):
                count_bad_fat -= 1
            left_border += 1
    return dynamic_ans


def task25():
    with open("24_5171.txt") as f:
        f = f.read()
    left_border, dynamic_ans, count_ca = 0, 0, 0  # not necessary two indicators?
    for right_border in range(1, len(f)):
        if f[right_border - 1] + f[right_border] == "CA":
            count_ca += 2
        elif right_border + 1 < len(f) and f[right_border + 1] == "C":
            count_ca += 1
            if count_ca > dynamic_ans:
                dynamic_ans = count_ca
            count_ca = 0
        if f[right_border] not in "CA":
            if count_ca > dynamic_ans:
                dynamic_ans = count_ca
            count_ca = 0
    return dynamic_ans


def task26():
    with open("24_2425.txt") as f:
        f = f.read()
    no_dynamic_ans, count_db_ac = 0, 0  # no dynamic count-count is full trash; as this realisation....
    while "DBAC" in f:
        f = f.replace("DBAC", "....")
    for ind in range(len(f)):
        if f[ind] == ".":
            count_db_ac += 1
        else:
            count_db_ac = count_db_ac + ((ind < len(f)) and f[ind] == "D") + \
                          ((ind + 1 < len(f)) and f[ind + 1] == "B") + ((ind + 2 < len(f)) and f[ind + 2] == "A")
            if count_db_ac > no_dynamic_ans:
                no_dynamic_ans = count_db_ac
            count_db_ac = 0
    """KABANOV'S REALISATION; МЕТОД ПЕРЕБОРА
    "DBAC" * n + "DBA" in f  # checking if true and changing while is not true
    """
    return no_dynamic_ans, len("DBAC" * 23 + "DBA")


def task27():
    # with open("24_2428.txt") as f:  # МЕТОДОМ КАБАНОВА ШМАЛЯЮ
    #    f = f.read()
    # print("YZ" + "XYZ" * 22 + "X" in f)
    return len("YZ" + "XYZ" * 22 + "X")


def task28():
    with open("24_18597.txt") as f:
        orig_f = f = f.read()
    f = f.split("&")
    ans = 0  # Важное примечание, при решении не regex, надо проверить на случай 4444.542254.2425 во втором Вещ. Числе
    for ind in range(1, len(f)):
        if len(f[ind - 1].split(".")) == 2 and f[ind - 1].split(".")[0].isdigit() and len(f[ind - 1].split(".")[0]) == 4 and \
                len(f[ind].split(".")) >= 2 and f[ind].split(".")[0].isdigit() and len(f[ind].split(".")[0]) == 4 and \
                len(f[ind - 1]) + len(f[ind]) + 1 > ans:
            ans = len(f[ind - 1]) + 1 + len(f[ind].split(".")[0]) + 1 + len(f[ind].split(".")[1])
    regex_expr = max(re.findall(r"[1-9]\d{3}\.\d+&[1-9]\d{3}\.\d+", orig_f), key=len)
    return ans, regex_expr, len(regex_expr)  # re выражения рулят, не забывать о возможности их применения


def task29():
    with open("24_19969.txt") as f:
        f = f.read()
    return len(max(re.findall(r"[a-z]+@[a-z]+\.[a-z]+", f), key=len))


def task30():
    with open("24_19967.txt") as f:
        f = f.read()
    return len(max(re.findall(r"AFD(?:[A-F]|\d)*(?:(?:[+*][1-9]\d*)|(?:[+*]0))*", f), key=len))  # noqa


def task31():
    with open("24_19968.txt") as f:
        f = f.read()
    return len(max(re.findall(r"(?:[1-5](?:[0-5]*))+(?:(?:[+*][1-5][0-5]*)|(?:[+*]0))*", f), key=len))


def task32():
    with open("24_19970.txt") as f:
        f = f.read()
    return len(max(re.findall(r"(?:[1-9]?\d*[05])+(?:[+*](?:(?:[1-9]+\d*[05])|[05]))*", f), key=len))


if __name__ == "__main__":
    """
    NOTE: В подобных задачах строки могут накладываться друг на друга
    поэтому лучшем решением будет являться выводить саму строку для проверки ее валидности
    или использовать while "NN" in s: s = s.replace("NN", "N N") или просто s.replace("NN", "N N").replace("NN", "N N")
    ПРИМЕЧАНИЯ ПРИ ПРИМЕНЕНИИ Regex expressions (https://regex101.com):
    1. всегда проверять expr с соответствием условий задачи + смотреть на саму строку + перечитывать условие задачи
    """
    print("#1", task1())
    print("#2", task2())
    print("#3", task3())
    print("#4", task4())
    print("#5", task5())
    print("#6", task6())
    print("#7", task7())
    print("#8", task8())
    print("#9", task9())
    print("#10", task10())
    print("#11", task11())
    print("#12", task12())
    print("#13", task13())
    print("#14", task14())
    print("#15", task15())
    print("#16", task16())
    print("#17", task17())
    print("#18", task18())
    print("#19", task19())
    print("#20", task20())
    print("#21", task21())
    print("#22", task22())
    print("#23", task23())
    print("#24", task24())
    print("#25", task25())
    print("#26", task26())
    print("#27", task27())
    print("#28", task28())
    print("#29", task29())
    print("#30", task30())
    print("#31", task31())
    print("#32", task32())
