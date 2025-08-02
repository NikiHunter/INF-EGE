from functools import lru_cache


@lru_cache()
def f(num: int):
    if num == 0:
        return 0
    if num % 2 == 0:
        return f(num // 2)
    return 1 + f(num - 1)


count = 0
for n in range(1, 501):
    if f(n) == 3:
        count += 1
print(count)
