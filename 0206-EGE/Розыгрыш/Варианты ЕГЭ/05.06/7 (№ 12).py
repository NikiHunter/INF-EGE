for n in range(4, 10000):
    tmp_str = "5" + "2" * n
    while "52" in tmp_str or "1122" in tmp_str or "2222" in tmp_str:
        tmp_str = tmp_str.replace("52", "11", 1)
        tmp_str = tmp_str.replace("2222", "5", 1)
        tmp_str = tmp_str.replace("1122", "25", 1)
    if sum([int(i) for i in tmp_str]) == 64:
        print(n)
        break
