def int_to_hex(n: int) -> str:
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary


for i in range(2, 255):
    b = int_to_hex(i) + int_to_hex(i)[:2]
    if i % 3:
        b = int_to_hex(i) + int_to_hex((i % 3) * 10)
    if int(b, base=6) > 680:
        print(int(b, base=6))
        break
