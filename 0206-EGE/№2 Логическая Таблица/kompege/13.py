from itertools import product, permutations


def f(x, y, z, w):
    return ((w <= y) or (not (y <= z))) and (not x) and (not (x == z))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(0, a1, 1, a2), (1, a3, a4, 1), (0, a5, 1, 1)]

    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print("".join(p))
