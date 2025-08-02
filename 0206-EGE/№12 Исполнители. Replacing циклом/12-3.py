stringy = "1" + "0" * 33
while "1" in stringy or "100" in stringy:
    if "100" in stringy:
        stringy = stringy.replace("100", "0001")
    else:
        stringy = stringy.replace("1", "00")
print(len(stringy))
