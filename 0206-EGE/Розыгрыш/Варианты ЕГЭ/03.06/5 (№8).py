from itertools import product


count = 0
for p in product([i for i in "ТИМОФЕЙ"], repeat=5):
    if p[0] != "Й" and p[-1] != "Й" and p.count("Й") <= 1 and 'ИЙ' not in ''.join(p) and 'ЙИ' not in ''.join(p):
        """
        (("".join(p).find("Й") != 4 and p["".join(p).find("Й") + 1] != "И") or "".join(p).find("Й") == 4) and \
            (("".join(p).find("Й") != 0 and p["".join(p).find("Й") - 1] != "И") or "".join(p).find("Й") == 0)
        """
        count += 1
print(count)
