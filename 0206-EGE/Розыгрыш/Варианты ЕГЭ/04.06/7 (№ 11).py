from math import ceil, log2

print(32768 * ceil(ceil(log2(1100)) * 107 / 8) / 2 ** 10)