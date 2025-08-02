a = []
for i in range(4, 999):
    print(bin(i))
    if sum([int(i) for i in bin(i)[2:]]) % 2:
        b = bin(i)[2:] + "1"
        b = "11" + b[2:]
    else:
        b = bin(i)[2:] + "0"
        b = "10" + b[2:]
    print(b)
    print(int(b, 2) if int(b, 2) < 20 else "")
    if int(b, 2) < 20:
        a.append(i)
print(max(a))
# 1503
