def to_4(num: int, to_bin=4) -> str:
    tmp_str = ""
    while num > 0:
        tmp_str += str(num % to_bin)
        num //= to_bin
    return tmp_str


num_ex = 3 * 16 ** 8 - 4 ** 5 + 3
print(to_4(num_ex).count("3"))
