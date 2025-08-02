from itertools import permutations


def f(a, b, c, d):
    return ((a and b) == (not c)) and (b <= d)


table = [(1, 0, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0)]
for p in permutations("abcd"):
    if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1, 1]:
        print("".join(p))
