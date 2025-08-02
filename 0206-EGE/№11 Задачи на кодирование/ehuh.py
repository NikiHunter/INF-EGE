def int_to_ternary(n: int) -> str:
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary


a = []
for i in range(4, 255):
    b = "1" + int_to_ternary(i) + "02"
    if i % 3:
        b = int_to_ternary(i) + int_to_ternary((i % 3) * 4)
    if int(b, 3) < 199:
        a.append(i)
print(max(a))
