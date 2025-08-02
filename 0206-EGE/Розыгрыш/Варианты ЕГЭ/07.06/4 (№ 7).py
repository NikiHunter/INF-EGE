from math import log2, ceil
print(750 * 2 ** 13 / (1024 * 768 * ceil(log2(256)) * 0.85))
