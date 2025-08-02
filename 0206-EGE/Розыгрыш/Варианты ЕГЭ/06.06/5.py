from itertools import product


count = 0
for i in product([0, 1, 2, 3, 4, 5, 6, 7, 8], repeat=5):
    # print(i)
    a = ''.join(map(str, i))
    if a.count("3") == 2:
        c = True
        for ind in range(len(a)):
            if a[ind] == "2" and ((ind != 0 and a[ind - 1] not in ["1", "3", "5", "7"]) or ind == 0) and \
                    ((ind != 4 and a[ind + 1] not in ["1", "3", "5", "7"]) or ind == 4):
                pass
            elif a[ind] == "2":
                c = False
        if c:
            count += 1
print(count)
