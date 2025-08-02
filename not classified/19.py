def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


ans = []
for num in range(245690, 245756 + 1):
    if is_prime(num):
        ans.append(num)
for i, res in enumerate(ans, start=1):
    print(i, res)
