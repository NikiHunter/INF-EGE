from itertools import product


for ind, p in enumerate(sorted(product("БАТЫР", repeat=5))):
    p_ = "".join(p)
    if "Ы" in p_ and "АА" not in p_:
        print(ind + 1, p_)
        break
