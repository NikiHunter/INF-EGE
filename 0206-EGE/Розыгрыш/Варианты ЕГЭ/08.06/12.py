def is_prime(num: int):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


for n in range(0, 100):
    tmp_str = ">" + "1" * n + 39 * "2" + "0" * 39
    while ">1" in tmp_str or ">2" in tmp_str or ">0" in tmp_str:
        tmp_str = tmp_str.replace(">1", "22>", 1)
        tmp_str = tmp_str.replace(">2", "2>", 1)
        tmp_str = tmp_str.replace(">0", "1>", 1)
    print(tmp_str, n)
    if is_prime(sum(int(i) for i in tmp_str[:-1])):
        print(n, sum(int(i) for i in tmp_str[:-1]))
        break
