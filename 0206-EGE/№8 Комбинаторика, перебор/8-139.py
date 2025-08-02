from itertools import product


b_ = [i for i in "НИСЕЙ"]
c = 0
for i in product(b_, repeat=4):
    if i[0] != "Й":
        if "1" in "".join(i).replace("Е", "1").replace("И", "1"):
            c += 1
print(c)  # 446
