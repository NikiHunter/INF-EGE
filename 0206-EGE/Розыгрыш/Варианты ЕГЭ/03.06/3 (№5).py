res = []

for n in range(1, 50000):
    r = bin(n)[2:]
    r = r + ("1" if r.count("1") % 2 == 0 else "0")
    r = r + ("1" if r.count("1") % 2 == 0 else "0")
    if int(r, 2) > 54:
        res.append(int(r, 2))
print(min(res))
