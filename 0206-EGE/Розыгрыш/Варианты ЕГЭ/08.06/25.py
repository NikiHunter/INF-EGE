def divs(num: int) -> tuple[int, int] | None:
    ans = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ans.append(num // i)
            ans.append(i)
    return (min(ans), max(ans)) if len(ans) else None


def is_prime(num: int):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for x in range(1, 900_000):
    get_div = divs(x)
    s = get_div[0] ** 2 + get_div[1] ** 2 if get_div else 4
    if is_prime(s):
        print(x, s)
        input()
