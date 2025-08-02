import math
import matplotlib.pyplot as plt
from shapely.geometry import Polygon


# Функция для поворота координат на угол
def rotate_point(x, y, angle):
    angle_rad = math.radians(angle)
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return x_new, y_new


# Функция для выполнения команд и симуляции пути
def simulate_turtle(commands):
    # Начальные значения
    x, y = 0, 0
    direction = 90  # Черепаха изначально направлена вверх (90 градусов)
    tail_down = False  # Хвост не опущен
    path = []  # Массив для хранения точек пути, когда хвост опущен

    # Обработаем команды
    for command in commands:
        if command[0] == "Вперёд":
            # Перемещение вперёд
            n = command[1]
            dx, dy = rotate_point(0, n, direction)
            x += dx
            y += dy
            if tail_down:
                path.append((x, y))
        elif command[0] == "Назад":
            # Перемещение назад
            n = command[1]
            dx, dy = rotate_point(0, -n, direction)
            x += dx
            y += dy
            if tail_down:
                path.append((x, y))
        elif command[0] == "Направо":
            # Поворот направо
            m = command[1]
            direction -= m
        elif command[0] == "Налево":
            # Поворот налево
            m = command[1]
            direction += m
        elif command[0] == "Поднять хвост":
            # Поднятие хвоста (прекращаем рисовать)
            tail_down = False
        elif command[0] == "Опустить хвост":
            # Опускание хвоста (начинаем рисовать)
            tail_down = True
        elif command[0] == "Повтори":
            # Повторение команд
            k = command[1]
            subcommands = command[2]
            for _ in range(k):
                for subcommand in subcommands:
                    commands.append(subcommand)

    return path


# Разбор команд и выполнение симуляции
commands = [
    ("Повтори", 9, [("Вперёд", 22), ("Направо", 90), ("Вперёд", 6), ("Направо", 90)]),
    ("Поднять хвост",),
    ("Вперёд", 1), ("Направо", 90), ("Вперёд", 5), ("Налево", 90), ("Опустить хвост",),
    ("Повтори", 9, [("Вперёд", 53), ("Направо", 90), ("Вперёд", 75), ("Направо", 90)])
]

# Получаем путь
path = simulate_turtle(commands)

# Создаем полигон из пути, чтобы вычислить периметр
polygon = Polygon(path)
perimeter = polygon.length

# Рисуем путь
x_points, y_points = zip(*path)
plt.plot(x_points, y_points, label="Путь Черепахи")
plt.fill(x_points, y_points, alpha=0.2, color='lightblue')
plt.title(f"Периметр области пересечения: {perimeter:.2f}")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
