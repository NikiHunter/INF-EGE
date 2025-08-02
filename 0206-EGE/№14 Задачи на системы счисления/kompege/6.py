def to_15(num: int, to_bin=15):
    tmp_str = []
    while num > 0:
        tmp_str.append(str(num % to_bin))  # СЛИВАЮТСЯ ЧИСЛА, ТАК ЧТО ДЕЛАЕМ ДЖАГА-ДЖАГА
        num //= to_bin
    return tmp_str


num_ex = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
print(res := to_15(num_ex))
print(len(set(res)))  # ВСЕГДА СМОТРИМ НА сам num_ex
