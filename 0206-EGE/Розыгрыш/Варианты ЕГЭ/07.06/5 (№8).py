from itertools import product


count = 0
for a in product([i for i in "МАНГУСТ"], repeat=6):
    if a[0] != "А" and a.count("У") >= 1 and a.count("М") == 2:
        count += 1
print(count)

count = 0
for a1 in [i for i in "МАНГУСТ"]:  # ПРОВЕРЯТЬ НА КИРИЛЛИЦУ!!!!!!!!!!!
    for a2 in [i for i in "МАНГУСТ"]:
        for a3 in [i for i in "МАНГУСТ"]:
            for a4 in [i for i in "МАНГУСТ"]:
                for a5 in [i for i in "МАНГУСТ"]:
                    for a6 in [i for i in "МАНГУСТ"]:
                        p = a1 + a2 + a3 + a4 + a5 + a6
                        if p[0] != "А" and p.count("У") >= 1 and p.count("М") == 2:
                            count += 1
print(count)
