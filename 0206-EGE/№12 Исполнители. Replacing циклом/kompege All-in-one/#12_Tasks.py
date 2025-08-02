def task4():
    init_str = "1" * 46 + "2" * 31
    while "1111" in init_str:
        init_str = init_str.replace("1111", "2", 1)
        init_str = init_str.replace("222", "1", 1)
    return init_str


def task6():
    init_str = ">" + 30 * "3" + 12 * "2" + 11 * "1"
    while ">1" in init_str or ">2" in init_str or ">3" in init_str:
        init_str = init_str.replace(">1", "22>", 1)
        init_str = init_str.replace(">2", "2>", 1)
        init_str = init_str.replace(">3", "1>", 1)
    return sum(int(i) for i in init_str[:-1])


def task7():
    for x in range(1, 50):
        for y in range(1, 50):
            for z in range(1, 50):
                init_str = "0" + "1" * x + "2" * y + "3" * z
                while "01" in init_str or "02" in init_str or "03" in init_str:
                    init_str = init_str.replace("01", "302")
                    init_str = init_str.replace("02", "3103")
                    init_str = init_str.replace("03", "20")
                if init_str.count("1") == 28 and init_str.count("2") == 34 and init_str.count("3") == 45:
                    return x, y, z


def task8():
    init_str = "1121121121121111"  # подбором // логикой!
    # print(init_str.count("1") == 12, init_str.count("2") == 4)  # checking
    while "11" in init_str:
        init_str = init_str.replace("112", "7")
        init_str = init_str.replace("11", "3")
        """ correctly will be:
        if "112" in init_str:
            init_str = init_str.replace("112", "7", 1)
        else:
            init_str = init_str.replace("11", "3", 1)
        """
    return sum(int(i) for i in init_str)


def task9():
    init_str = "9992" * 33 + "9" + "2" * 15 + "1" * 14  # maximizing count one's
    while "999" in init_str or "22" in init_str:
        if "999" in init_str:
            init_str = init_str.replace("999", "12", 1)
        else:
            init_str = init_str.replace("22", "1", 1)
    return init_str.count("1")


def task10():
    tmp_l = []
    for i in range(1, 100):
        init_str = "5" * i
        while "555" in init_str or "888" in init_str:
            init_str = init_str.replace("555", "8", 1)
            init_str = init_str.replace("888", "55", 1)
        if init_str in tmp_l:
            break
        tmp_l.append(init_str)
    return len(tmp_l)


def task11():
    for a in range(1, 50):
        for b in range(1, 50):
            x, y = -7, -1
            n = 15
            for _ in range(n):
                x, y = x + 15, y + 22
                x, y = x - a, y - b
            x, y = x + 23, y - 32
            if x == 1 and y == -3:
                return a, b, n  # 15


def task12():
    x, y = 3, -6
    n = 10 // 2
    b = 2
    for _ in range(n):
        x, y = x + 10, y - 6 + b
    x, y = x - 53, y + 26
    return x, y, b  # 2


if __name__ == "__main__":
    print("#4", task4())
    print("#6", task6())
    # print("#7", task7())
    print("#8", task8())
    print("#9", task9())
    print("#10", task10())
    print("#11", task11())
    print("#12", task12())
