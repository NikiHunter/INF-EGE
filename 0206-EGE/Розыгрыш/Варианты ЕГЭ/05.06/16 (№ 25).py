def dividers(num: int) -> list:
    ans = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            ans.append(num // i)
            ans.append(i)
    return list(set(ans))


for i in range(600_000, 1_000_000):
    divs = [x for x in dividers(i) if str(x)[-1] == "7" and x != 7 and x != i]
    min_div = min(divs) if divs else None
    if min_div:
        print(i, min_div)
        input()
