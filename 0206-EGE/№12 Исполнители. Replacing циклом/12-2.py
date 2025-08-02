stringy = "2" + "5" * 81
while "25" in stringy or "355" in stringy or "4555" in stringy:
    if "25" in stringy:
        stringy = stringy.replace("25", "4")
    elif "355" in stringy:
        stringy = stringy.replace("355", "2")
    elif "4555" in stringy:
        stringy = stringy.replace("4555", "3")
print(stringy)