for n in range(1, 5000):
    r = bin(n)[2:]
    r += r[:2][::-1]
    if int(r, 2) > 74:
        print(n)
        break
