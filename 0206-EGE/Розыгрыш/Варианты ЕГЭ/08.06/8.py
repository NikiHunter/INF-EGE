from itertools import product

count = 0
for a1, a2, a3, a4, a5, a6 in product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], repeat=6):
    p = [a1, a2, a3, a4, a5, a6]
    if p.count(7) == 1 and a1 != 0 and len([x for x in p if x > 9]) <= 3:
        count += 1
print(count)
