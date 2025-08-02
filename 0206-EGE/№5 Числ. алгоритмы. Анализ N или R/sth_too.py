a = []
for i in range(1, 100):
    b = bin(i) + str(bin(i).count("1") % 2) + "0"
    if int(b, 2) < 80:
        a.append(int(b, 2))
        print(int(b, 2))
print(len(a), a)