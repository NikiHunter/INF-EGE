stringy = "8" * 70
while "2222" in stringy or "8888" in stringy:
    if "2222" in stringy:
        stringy = stringy.replace("2222", "88")
    else:
        stringy = stringy.replace("8888", "22")
print(stringy)
