from itertools import product


b_ = [i for i in "МАРИЯ"]
a = 0
for i, n in enumerate(sorted(product(b_, repeat=4))):
    if i == 210:
        a = n
print(a)
