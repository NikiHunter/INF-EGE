def int_to_ternary(n: int) -> str:
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary


for i in range(1, 100):
    b = int_to_ternary(i) + str(i % 3)
    if int(b, 3) >= 100:
        print(int(b, 3))
        break
