with open("1_24.txt") as f:
    f = f.read()


left_d, dynamic_ans, count_d = 0, 0, 0
for right_d in range(len(f)):
    if f[right_d] == "T":
        count_d += 1
    while count_d > 150:
        if f[left_d] == "T":
            count_d -= 1
        left_d += 1
    if right_d - left_d + 1 > dynamic_ans:
        dynamic_ans = right_d - left_d + 1
print(dynamic_ans)
# ЗАПОМНИТЬ АЛГОРИТМ ДВУХ УКАЗАТЕЛЕЙ, МОЖЕТ, ВИДОС ПОСМОТРЕТЬ
