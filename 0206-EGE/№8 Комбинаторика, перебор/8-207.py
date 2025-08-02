from itertools import product


b_ = [i for i in "РЕЖИМДНО"]  # ... РЕЖИМ - ДНО!
c = 0
for i in product(b_, repeat=6):
    if len(set(i)) == len(i):
        f_ = "".join(i).replace("Р", "0").replace("Ж", "0").replace("М", "0").replace("Д", "0").replace("Н", "0")
        f_ = f_.replace("Е", "1").replace("И", "1").replace("О", "1")
        if f_[:2] == "01" and f_[-1] == "1":
            c += 1
print(c)  # 1800
