from math import dist

clusterA, clusterB = [[], []], [[], [], []]
with open("27А.txt") as f:
    for i in f.readlines():
        x, y = list(map(float, i.replace(",", ".").split()))
        clusterA[0 if x > 3 else 1].append([x, y])
with open("27Б.txt") as f:
    for i in f.readlines():
        x, y = list(map(float, i.replace(",", ".").split()))
        clusterB[0 if x > 4 else 1 if y > 2.3 else 2].append([x, y])


def min_point(cl):
    return min([p for p in cl], key=lambda p1: sum(dist(p1, q) for q in cl))


minA = [min_point(clA) for clA in clusterA]
minB = [min_point(clB) for clB in clusterB]
print(sum([i[0] for i in minA]) / 2 * 10000, sum([i[1] for i in minA]) / 2 * 10000)
print(sum([i[0] for i in minB]) / 3 * 10000, sum([i[1] for i in minB]) / 3 * 10000)
