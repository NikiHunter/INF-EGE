import re


with open("107_24.txt") as f:
    f = f.read()
matched_ = re.findall(r'(?:(?:AB)|(?:CB))+', f)
print(len(max(matched_, key=lambda x: len(x))) // 2)
