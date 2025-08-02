ans = []
for x in range(0, 9):
    for y in range(0, 12):
        tmp_str = 2 * 9 ** 4 + y * 9 ** 3 + 6 * 9 ** 2 + 6 * 9 ** 1 + x * 9 ** 0 + \
                  x * 12 ** 3 + 0 * 12 ** 2 + y * 12 ** 1 + 1 * 12 ** 0
        if tmp_str % 170 == 0:
            ans.append(tmp_str // 170)
print(min(ans))
