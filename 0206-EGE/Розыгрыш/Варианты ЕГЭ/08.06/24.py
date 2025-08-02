import re


with open("24.txt") as f:
    f = f.read()

re_match = re.findall(r"(?:(?:[1234]\d*)|0)(?:(?:[+-](?:[1234]\d*))|(?:[+-]0))*", f)
print(len(max(re_match, key=lambda x: len(x))))
# max_len, ans = "", ""
# for i in f:
#     if i.isdigit():
#         if len(max_len) >= 1 and (max_len[-1] == "0" == i or (len(max_len) == 1 and max_len[-1] in "+-")):
#             ans = max_len if len(max_len) > len(ans) else ans
#             max_len = ""
#         elif len(max_len) >= 1 and max_len[-1] == "0" and i != "0" and \
#                 not (len(max_len) >= 2 and max_len[-2] not in "0+-"):  # ЗДЕСЬ НЕ УЧИТЫВАЕТСЯ 13000000000....
#             ans = max_len if len(max_len) > len(ans) else ans
#             max_len = ""
#         max_len += i
#     elif i in "+-":
#         if len(max_len) >= 1 and max_len[-1] in "+-":
#             ans = max_len if len(max_len) > len(ans) else ans
#             max_len = ""
#         max_len += i
# print(len(ans), ans)
