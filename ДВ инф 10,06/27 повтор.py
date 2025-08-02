from math import dist


with open("27B_18056.txt") as f:  # "27B.txt"
    f.readline()
    all_points = [list(map(float, i.replace(",", ".").split())) for i in f.readlines()]

clusters = []
while len(all_points) > 0:
    clusters.append([all_points.pop(0)])
    for p in clusters[-1]:
        for p1 in all_points:
            if dist(p, p1) <= 0.7:  # 0.7 или 1 в зависимости от КОЛИЧЕСТВА ТОЧЕК АНОМАЛИЙ + КЛАСТЕРОВ СООТ. ИХ КОЛ-ВА
                clusters[-1].append(p1)
                all_points.remove(p1)

print([len(cl) for cl in clusters])  # СМОТРЕТЬ НА КОЛИЧЕСТВО КЛАСТЕРОВ
clusters = [cl for cl in clusters if len(cl) > 30]


def centroid(cl):
    return min(cl, key=lambda point_1: sum([dist(point_1, point_2) for point_2 in cl]))


min_points = [centroid(cl) for cl in clusters]
px = sum(x for x, y in min_points) / len(min_points)
py = sum(y for x, y in min_points) / len(min_points)

print(int(abs(px) * 100_000), int(abs(py) * 100_000))
