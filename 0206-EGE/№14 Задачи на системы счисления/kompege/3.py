def to_3(num: int, to_bin=3):
    tmp_str = ""
    while num > 0:
        tmp_str += str(num % to_bin)
        num //= to_bin
    return tmp_str[::-1]


num_ex = 2 * 27 ** 7 + 3 ** 10 - 9
print(to_3(num_ex).count("0"))
