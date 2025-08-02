import re

with open("24.txt") as f:
    f = f.read()

re_match = re.findall("(?:[CDF][AO])+", f)
print(len(max(re_match, key=lambda x: len(x))) // 2)
