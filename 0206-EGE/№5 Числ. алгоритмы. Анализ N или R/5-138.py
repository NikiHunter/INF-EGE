for n in range(1, 100):
    b = bin(n)
    b += b[-1]
    b += str(b.count("1") % 2)
    b += "0"
    if int(b, 2) > 114:
        print(int(b, 2))
        break
# Ответ: 126
