ans = []
for i in range(1, 50):
    s = "6" * i
    while "66" in s:
        s = s.replace("66", "1")
        s = s.replace("11", "2")
        s = s.replace("22", "6")
    if s == "21":
        ans.append(i)
print(max(ans))
