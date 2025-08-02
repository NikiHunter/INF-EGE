ari_fm = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024

res = ""
while ari_fm > 0:
    res += str(ari_fm % 25)
    ari_fm //= 25
print(res[::-1].count("0"), res[::-1])
