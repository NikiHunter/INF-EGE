def to_7(num: int, to_bin=7):
    tmp_str = ""
    while num > 0:
        tmp_str += str(num % to_bin)
        num //= to_bin
    return tmp_str[::-1]


num_ex = 51 * 7 ** 12 - 7 ** 3 - 22
print(sum(int(i) for i in to_7(num_ex)))
