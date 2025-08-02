def to_8(num: int, to_bin=8) -> str:
    tmp_str = ""
    while num:
        tmp_str += str(num % to_bin)
        num //= to_bin
    return tmp_str[::-1]


num_ex = 64 ** 30 + 2 ** 300 - 4
count_ex = to_8(num_ex).count("7")
print(count_ex)
