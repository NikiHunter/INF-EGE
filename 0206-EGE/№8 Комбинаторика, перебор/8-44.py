from itertools import product


b_ = [i for i in "КЛОУН"]
c = 0
for i in product(b_, repeat=4):
    if "У" in i:
        c += 1
print(c)  # 369
