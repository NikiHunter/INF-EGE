from math import log2, ceil

print(693 * 2 ** 13 / 2000 / ceil(log2(963 + 52 + 10)))
print(693 * 2 ** 10 / 2000, ceil(ceil(log2(963 + 52 + 10)) * 257 / 8))
