def main():
    s = open("24_19149.txt").read()
    n = len(s)
    if n == 0:
        print(0)
        return

    # Инициализация таблиц
    dpS = [[None] * n for _ in range(n)]
    dpT = [[None] * n for _ in range(n)]
    dpN = [[None] * n for _ in range(n)]

    # Префиксные суммы для проверки цифровых подстрок
    digit_arr = [1 if c in '1234' else 0 for c in s]
    prefix = [0] * (n + 1)
    for idx in range(1, n + 1):
        prefix[idx] = prefix[idx - 1] + digit_arr[idx - 1]

    # База: подстроки длины 1
    for i in range(n):
        if s[i] in '1234':
            parity = 1 if s[i] in '13' else 0
            dpN[i][i] = parity
            dpT[i][i] = parity
            dpS[i][i] = parity

    # Заполнение таблиц для длин от 2 до n
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            total_chars = L
            total_digits = prefix[j + 1] - prefix[i]
            if total_digits == total_chars:
                last_char = s[j]
                parity = 1 if last_char in '13' else 0
                dpN[i][j] = parity
                if dpT[i][j] is None:
                    dpT[i][j] = parity
                if dpS[i][j] is None:
                    dpS[i][j] = parity

            # Терм: '(' S ')'
            if s[i] == '(' and s[j] == ')':
                if i + 1 <= j - 1 and dpS[i + 1][j - 1] is not None:
                    dpT[i][j] = dpS[i + 1][j - 1]

            # Обновление S из T
            if dpT[i][j] is not None:
                if dpS[i][j] is None:
                    dpS[i][j] = dpT[i][j]

            # S -> T '+' S
            for k in range(i + 1, j):
                if s[k] == '+':
                    if dpT[i][k - 1] is not None and dpS[k + 1][j] is not None:
                        p_left = dpT[i][k - 1]
                        p_right = dpS[k + 1][j]
                        total_parity = (p_left + p_right) % 2
                        if dpS[i][j] is None:
                            dpS[i][j] = total_parity

            # Дополнительное обновление S из T
            if dpT[i][j] is not None and dpS[i][j] is None:
                dpS[i][j] = dpT[i][j]

    # Поиск максимальной длины подстроки
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] == '(' and s[j] == ')' and dpS[i][j] is not None and dpS[i][j] == 0:
                length = j - i + 1
                if length > max_len:
                    max_len = length

    print(max_len)


if __name__ == '__main__':
    main()
