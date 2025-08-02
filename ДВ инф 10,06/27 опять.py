from math import dist


with open("27B_18625.txt") as f:
    f.readline()
    all_points = [list(map(float, i.replace(",", ".").split())) for i in f.readlines()]

clusters = []
while len(all_points) > 0:  # ВЫТАСКИВАЕМ ПОКА МОЖЕМ ИЗ ВСЕХ ТОЧЕК
    clusters.append([all_points.pop(0)])  # СОЗДАЕМ ДЛЯ ТОЧКИ ОПРЕДЕЛЕННОЙ КЛАСТЕР
    for p in clusters[-1]:  # ПЕРЕБИРАЕМ ДЛЯ ЭТОЙ ТОЧКИ ЕЕ СОБРАТЬЕВ
        for p1 in all_points:  # ПРОХОДИМСЯ ПО ВСЕМ ТОЧКАМ ЕЕ
            if dist(p, p1) <= 1:  # СМОТРИМ ДИСТАНЦИЮ
                clusters[-1].append(p1)
                all_points.remove(p1)

print([len(cl) for cl in clusters])
clusters = [cl for cl in clusters if len(cl) > 30]


def min_point(cl):
    return min(cl, key=lambda point_1: sum([dist(point_1, point_2) for point_2 in cl]))


min_points = [min_point(cl) for cl in clusters]

px = sum(x for x, y in min_points) / len(min_points)
py = sum(y for x, y in min_points) / len(min_points)
print(int(px * 100_000), int(py * 100_000))
