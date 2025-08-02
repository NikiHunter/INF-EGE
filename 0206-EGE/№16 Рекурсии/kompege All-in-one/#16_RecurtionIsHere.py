from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(10000)


@lru_cache()
def task12(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return task12(n - 1) - task12(n - 2) + 3 * n


@lru_cache()
def task13(n: int):
    if n <= 18:
        return n + 3
    if n % 3 == 0:
        return (n // 3) * task13(n // 3) + n - 12
    return task13(n - 1) + n ** 2 + 5


@lru_cache()
def task14(n: int):
    if n <= 30 and n % 2:
        return 2 * task14(n + 2) + task14(n + 5)
    if n <= 30:
        return task14(n + 1) + 3 * task14(n + 4)
    return n ** 2 + 5 * n + 4


@lru_cache()
def task15(n: int):
    if n == 0:
        return 0
    if n % 2 == 0:
        return task15(n // 2)
    return 1 + task15(n - 1)


@lru_cache()
def task16(n: int):
    if n == 1:
        return 1
    if n % 2 == 0:
        return task16(n // 2) + 1
    return task16(n - 1) + n


@lru_cache()
def task17(n: int):  # Kabanov's algorithm
    k = 1
    if n >= 1:
        k += 2 + task17(n - 1) + task17(n - 3)
    return k


@lru_cache()
def task18(n: int):
    ans = n ** 2
    if n > 1:
        ans += 2 * n + 1 + task18(n - 2) + task18(n // 3)
    return ans


@lru_cache()
def task19(n: int):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + task19(n // 3)
    return n + task19(n + 3)


@lru_cache()
def task20(n: int):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return task20(n - 2) + n - 2
    return task20(n + 2) + n + 2


if __name__ == "__main__":
    print("#12", task12(40))
    task13_list = [str(task13(i)) for i in range(1, 1001)]
    print("#13", len([i for i in task13_list if len(i) == len([m for m in i if m in "24680"])]))  # Not working
    print("#14", len([i for i in range(1, 1001) if sum(map(int, [x for x in str(task14(i))])) == 27]))
    print("#15", len([i for i in range(1, 501) if task15(i) == 8]))
    print("#16", min([i for i in range(1, 501) if task16(i) == 19]))
    print("#17", task17(40))
    print("#18", task18(100))
    print("#19", task19(81))  # только степени тройки пролетают
    print("#20", len([i for i in range(0, 2_000_000, 2) if len(str(task20(i))) == 5]))
