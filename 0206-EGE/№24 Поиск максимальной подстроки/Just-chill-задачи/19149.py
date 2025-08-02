import re


with open("24_19149.txt") as f:
    f = f.read()


# i = 0
# tmp_str = ""
# max_len = 0
# for i in range(len(f)):
#     if f[i] == "(":
#         tmp_str += f[i]
#     elif f[i] == ")":
#         tmp_str += f[i]
#         while tmp_str.count("("):
#             tmp_str = tmp_str[tmp_str.find("(") + 1:]
#             if tmp_str.count("(") == tmp_str.count(")") and tmp_str[0] == "(":
#                 tmp_str = tmp_str[:tmp_str.find(")") + 1]
#                 if len(tmp_str) > max_len:
#                     try:
#                         ev = eval(tmp_str)
#                         if isinstance(ev, int) and ev % 2 == 0:
#                             max_len = len(tmp_str)
#                     except TypeError as e:
#                         print(tmp_str)
#                         input()
#     elif f[i] == "+":
#         if f[i - 1].isdigit() and (i + 1 < len(f) and f[i + 1].isdigit()):
#             tmp_str += f[i]
#         else:
#             tmp_str = ""
#     else:
#         tmp_str += f[i]
# print(max_len)
re_match = re.findall(r"(?:\d+|\((?:[+\-*/^]|\d+|\((?:\d+|\([^()]*\))*\))*\))(?:[+\-*/^](?:\d+|\((?:[+\-*/^]|\d+|\((?:\d+|\([^()]*\))*\))*\)))*", f)
print(len(max(re_match, key=lambda x: len(x) and isinstance(eval(x), int) and eval(x) % 2 == 0)))
