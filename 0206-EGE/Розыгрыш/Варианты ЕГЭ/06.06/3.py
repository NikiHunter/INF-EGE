def treen(num: int):
    tmp_str = ""
    while num > 0:
        tmp_str += str(num % 3)
        num //= 3
    return tmp_str[::-1]


ans = 0
for n in range(1, 10000):
    r = treen(n)
    r = r + (r[-2:] if n % 3 == 0 else treen((n % 3) * 5))
    if int(r, 3) <= 173:
        ans = int(r, 3) if int(r, 3) > ans else ans
print(ans)
