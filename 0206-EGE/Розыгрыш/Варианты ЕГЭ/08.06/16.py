from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(100000)


@lru_cache()
def f(num: int):
    if num == 1:
        return 1
    if num % 2 == 0:
        return 2 * num * f(num - 1) + f(num - 3)
    return f(num - 2) * 3


print(f(2026) / f(2021))
