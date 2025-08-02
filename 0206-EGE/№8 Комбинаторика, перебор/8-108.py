from itertools import product


b_ = [i for i in "КОМЕТА"]
c = 0
for i in product(b_, repeat=6):
    if len(set(i)) == len(i):
        f_ = "".join(i).replace("К", "0").replace("М", "0").replace("Т", "0")
        f_ = f_.replace("А", "1").replace("Е", "1").replace("О", "1")
        if "00" not in f_ and "11" not in f_:
            c += 1
print(c)
