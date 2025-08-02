from math import dist


with open("27A_18625.txt") as f:
    f.readline()
    all_points = [list(map(float, i.replace(",", ".").split())) for i in f.readlines()]

clusters = []
while len(all_points) > 0:
    clusters.append([all_points.pop(0)])
    for p in clusters[-1]:
        for p1 in all_points:
            if dist(p, p1) <= 1:  # ТУТ ЧЕКАТЬ и УМЕНЬШАТЬ ЕСЛИ НЕ ВСЕ АНОМАЛИИ ЗАШЛИ!
                clusters[-1].append(p1)
                all_points.remove(p1)

print([len(cl) for cl in clusters])  # ПРОВЕРИЛИ НА КОЛИЧЕСТВО И УБРАЛИ АНОМАЛИИ
clusters = [cl for cl in clusters if len(cl) > 30]


def min_point(cl):
    return min(cl, key=lambda point_1: sum([dist(point_1, point_2) for point_2 in cl]))


min_points = [min_point(cl) for cl in clusters]

px = sum(x for x, y in min_points) / len(clusters)
py = sum(y for x, y in min_points) / len(clusters)
print(int(px * 100_000), int(py * 100_000))
