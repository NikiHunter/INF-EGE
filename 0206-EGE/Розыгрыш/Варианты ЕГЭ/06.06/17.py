from math import dist


def min_point(cl):
    return min(cl, key=lambda q: sum(dist(p, q) for p in cl))


with open("1_27_A.txt") as f:
    with open("1_27_B.txt") as f2:
        f = [list(map(float, i.replace(",", ".").split())) for i in f.readlines()]
        f2 = [list(map(float, i.replace(",", ".").split())) for i in f2.readlines()]


clusterA = [[], []]
clusterB = [[], [], []]
for i in f:
    x, y = i
    clusterA[0 if y > 0 else 1].append([x, y])
for i in f2:
    x, y = i
    clusterB[0 if x > 20 else 1 if x > 15 else 2].append([x, y])


min_A = [min_point(cl_) for cl_ in clusterA]
min_B = [min_point(cl_) for cl_ in clusterB]
print(abs(sum([i[0] for i in min_A]) / 2) * 10000, abs(sum([i[1] for i in min_A]) / 2) * 10000)
print(abs(sum([i[0] for i in min_B]) / 3) * 10000, abs(sum([i[1] for i in min_B]) / 3) * 10000)
