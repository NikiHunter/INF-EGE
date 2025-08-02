a = []
for i in range(1, 255):
    b = "1" + bin(i)[2:] + "0"
    if int(bin(i)[2:], 2) % 2:
        b = "11" + bin(i)[2:] + "11"
    if int(b, 2) > 52:
        a.append(int(b, 2))
print(min(a))
