a = []
for i in range(4, 255):
    b = "10" + bin(i)[4:] + "0"
    if int(bin(i)[2:], 2) % 2:
        b = "11" + bin(i)[4:] + "1"
    if int(b, 2) < 35:
        a.append(i)
print(max(a))
