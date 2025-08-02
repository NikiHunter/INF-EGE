import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# Начальная позиция
x, y = 0, 0

# Список для хранения координат
points = [(x, y)]

# Алгоритм перемещения
for _ in range(10):
    # Сместиться на (3, 6)
    x += 3
    y += 6
    points.append((x, y))

    # Сместиться на (7, -2)
    x += 7
    y += -2
    points.append((x, y))

    # Сместиться на (-10, -4)
    x += -10
    y += -4
    points.append((x, y))

# Создаем многоугольник из полученных точек
polygon = Polygon(points)

# Определяем границы области
min_x, min_y, max_x, max_y = polygon.bounds

# Считаем целочисленные точки внутри многоугольника
count = 0
for i in range(int(min_x) + 1, int(max_x)):
    for j in range(int(min_y) + 1, int(max_y)):
        if polygon.contains(Point(i, j)):
            count += 1

print("Количество целочисленных точек внутри области:", count)

# Визуализация
x, y = zip(*points)
plt.plot(x, y, marker='o')
plt.fill(*polygon.exterior.xy, alpha=0.5)
plt.xlim(min_x - 1, max_x + 1)
plt.ylim(min_y - 1, max_y + 1)
plt.title("Путь Чертёжника")
plt.grid()
plt.show()
