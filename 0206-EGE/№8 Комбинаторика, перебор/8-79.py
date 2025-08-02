from itertools import product


b_ = [i for i in "ГОРА"]
c = 0
for i, j in enumerate(sorted(product(b_, repeat=4))):
    if "А" not in j:
        print(i + 1)  # (n - 1) + 1
        break
# 86
