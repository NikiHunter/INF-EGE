def func_task8(x: int, a: int):
    return (x & 107 == 0) <= (x & 55 != 0) <= (x & a != 0)


def task8():
    for a in range(1, 1_000):
        if all(func_task8(x, a) for x in range(1, 10_000)):
            return a


if __name__ == "__main__":
    print("#8", task8())
