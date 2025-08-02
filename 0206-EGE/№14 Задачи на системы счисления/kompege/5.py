def to_5(num: int, to_bin=5):
    tmp_str = ""
    while num > 0:
        tmp_str += str(num % to_bin)
        num //= to_bin
    return tmp_str[::-1]


for x in range(1, 1000):
    num_ex = 125 ** 200 - 5 ** x + 74
    if to_5(num_ex).count("4") == 100:
        print(x)
        break
