a = []
for n in range(1, 100):
    b = bin(n) + ("10" if bin(n)[-1] == "1" else "01")
    if int(b, 2) > 97:
        a.append(n)
print(min(a))
# Ответ: 25
