str_ = "1" + 100 * "9"

while "19" in str_ or "299" in str_ or "3999" in str_:
    str_ = str_.replace("19", "2", 1)
    str_ = str_.replace("299", "3", 1)
    str_ = str_.replace("3999", "1", 1)
print(str_)
