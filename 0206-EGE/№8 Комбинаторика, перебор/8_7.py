from itertools import product


b_ = [i for i in "АБИКЛОУН"]
c = 0
for i in product(b_, repeat=8):
    if len(set(i)) == len(i):
        f_ = "".join(i).replace("Б", "0").replace("К", "0").replace("Л", "0").replace("Н", "0")
        f_ = f_.replace("А", "1").replace("И", "1").replace("О", "1").replace("У", "1")
        if "00" not in f_ and "11" not in f_:
            c += 1
print(c)
