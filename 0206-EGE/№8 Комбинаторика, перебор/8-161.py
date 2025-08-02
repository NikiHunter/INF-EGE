from itertools import product


b_ = [i for i in "01234567"]
c = 0
for i in product(b_, repeat=6):
    if len(set(i)) == len(i) and i[0] != "0":
        f_ = "".join(i).replace("2", "0").replace("4", "0").replace("6", "0")
        f_ = f_.replace("3", "1").replace("5", "1").replace("7", "1")
        if "00" not in f_ and "11" not in f_:
            c += 1
print(c)  # 1008
