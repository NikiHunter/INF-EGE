with open("27_a.txt") as f:
    clustersA = [[], []]
    for i in f.readlines():
        x, y = map(float, i.strip().replace(",", ".").split())
        if y >= 15:
            clustersA[0].append([x, y])
        else:
            clustersA[1].append([x, y])
with open("27_b.txt") as f:
    clustersB = [[], [], []]
    for i in f.readlines():
        x, y = map(float, i.strip().replace(",", ".").split())
        if x > 0:
            clustersB[0].append([x, y])
        elif y > 2:
            clustersB[1].append([x, y])
        else:
            clustersB[2].append([x, y])


def calc_dist(tp: tuple[float, float], tp2: tuple[float, float]):
    x1, y1, x2, y2 = *tp, *tp2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def find_center(cluster):
    res = []
    for tp_ in cluster:
        dist_ = sum(calc_dist(tp_, tp2_) for tp2_ in cluster)
        res.append([dist_, tp_])
    return min(res)[1]


ans_A = [find_center(cl_) for cl_ in clustersA]
px_A = abs(int(sum(x for x, y in ans_A))) * 10000
py_A = abs(int(sum(y for x, y in ans_A))) * 10000
print(px_A, py_A)

ans_B = [find_center(cl_) for cl_ in clustersB]
px_B = abs(int(sum(x for x, y in ans_B))) * 10000
py_B = abs(int(sum(y for x, y in ans_B))) * 10000
print(px_B, py_B)
# СМОТРЕТЬ СТРИМ КАБАНОВА ПО 27 и др.
