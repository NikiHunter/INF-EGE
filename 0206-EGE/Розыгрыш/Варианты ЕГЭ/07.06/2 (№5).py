min_ans = 10000

for n in range(1, 10000):
    r = bin(n)[2:]
    r = r + str(sum(int(i) for i in str(n)) % 2)
    r = r + str(sum(int(i) for i in str(int(r, 2))) % 2)
    r = r + str(sum(int(i) for i in str(int(r, 2))) % 2)
    if int(r, 2) > 2054:
        min_ans = int(r, 2) if int(r, 2) < min_ans else min_ans
print(min_ans)
