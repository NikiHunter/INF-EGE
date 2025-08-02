with open("24.txt") as f:
    f = f.read()


f = f.replace("A", "C").replace("B", "C")
max_c = 0
tmp_str = ""
for i in f:
    if tmp_str and tmp_str[-1] == i == "C":
        if len(tmp_str) > max_c:
            max_c = len(tmp_str)
        tmp_str = ""
    tmp_str += i
print(max_c)
