tmp_str = "1x24A + x2024 – 6x08"
first, second, third = "1x24A", "x2024", "6x08"
for x in range(0, 46):  # ЗАПОМНИТЬ ОСОБЕННОСТИ СИСТЕМЫ СЧИСЛЕНИЯ!!!!
    first_ = (1 * 47 ** 4 + x * 47 ** 3 + 2 * 47 ** 2 + 4 * 47 ** 1 + 10 * 47 ** 0)
    second_ = (x * 47 ** 4 + 2 * 47 ** 3 + 0 * 47 ** 2 + 2 * 47 ** 1 + 4 * 47 ** 0)
    third_ = (6 * 47 ** 3 + x * 47 ** 2 + 0 * 47 ** 1 + 8 * 47 ** 0)
    res = first_ + second_ - third_
    if res % 46 == 0:
        print(x)
        break
