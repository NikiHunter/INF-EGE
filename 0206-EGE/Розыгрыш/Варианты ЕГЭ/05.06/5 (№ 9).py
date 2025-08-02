with open("9.txt") as f:
    f = [list(map(int, i.split("\t"))) for i in f.readlines()]

count = 0
for i in f:
    if (i.count(max(i)) == 1 and [i.count(x) for x in i if i.count(x) > 1] and
            max(i) > ((sum(i) - max(i)) / (len(i) - 1)) * 3):
        count += 1
print(count)
