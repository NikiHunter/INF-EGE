for i in range(1, 255):
    b = bin(i * 2) + str(bin(i * 2).count("1") % 2) + "0"
    if int(b, 2) > 1017:
        print(i)
        break
