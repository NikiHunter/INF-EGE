# Функция для обработки файла и поиска пары

def find_max_sum_pair(filename):
    with open(filename, 'r') as f:
        data = f.readlines()

    # Считываем количество чисел
    n = int(data[0])
    numbers = list(map(int, data[1:]))

    max_sum = 0
    best_pair = (0, 0)

    # Перебор всех пар чисел
    for i in range(n):
        for j in range(i + 1, n):
            a, b = numbers[i], numbers[j]

            # Условие: разные остатки от деления на 160 и хотя бы одно делится на 7
            if (a % 160 != b % 160) and (a % 7 == 0 or b % 7 == 0):
                current_sum = a + b
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_pair = (min(a, b), max(a, b))

    return best_pair

# Путь к файлам
file_a = 'A.txt'
file_b = 'B.txt'

# Обработка файлов
result_a = find_max_sum_pair(file_a)
result_b = find_max_sum_pair(file_b)

# Вывод результатов
print(result_a[0], result_a[1], result_b[0], result_b[1])