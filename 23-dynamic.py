"""
def f(c, e):
    if int(c, 2) > int(e, 2) or c in []: return 0
    if int(c, 2) == int(e, 2): return 1
    if int(c, 2) < int(e, 2): return f(bin(int(c,2) + 1)[2:], e) + f(c + "0", e) + f(c + "1", e)


print(f("100", "11101"))

"""
"""
def f(c, e):
    if c > e or c in []: return 0
    if c == e: return 1
    if c < e: return f(c+1, e) + f(c + 10 + (1 if str(c + 1)[0] == str(c)[0] else 0), e)


print(f(25, 51))
"""
"""
def f(c, e):
    if c > e or c in []: return 0
    if c == e: return 1
    if c < e: return f(c+1, e) + (f(c * 1.5, e) if c % 2 == 0 else 0)


print(f(1, 20))
"""
"""
def f(c, e):
    if c > e or c in []: return 0
    if c == e: return 1
    if c < e: return f(c+2, e) + f(c + 4, e) + f(c+5, e)



for i in range(34, 340):
    if f(31, i) == 1001:
        print(i)
        break
"""
"""
def f(c, e, path_):
    if c > e or c in [] or path_ < 0: return 0
    if c == e and path_ == 0: return 1
    if c == e and path_ > 0: return 0
    if c < e:
        return f(c * 2 + 1, e, path_ - 1) + f(c * 2, e, path_ - 1)



print(f(3, 27, 7))
"""
"""
ans = set()


def f(c, e, path_):
    if path_ == 0:
        ans.add(c)
        return
    f(c * 2 + 1, e, path_ - 1)
    f(c * 2, e, path_ - 1)


f(1, float('inf'), 15)
print(len(ans))
"""
"""
ans = set()


def f(c, e, path_):
    if path_ == 0:
        if 1000 <= c <= 1024:
            ans.add(c)
        return
    f(c + 1, e, path_ - 1)
    f(c + 5, e, path_ - 1)
    f(c * 3, e, path_ - 1)


f(1, float('inf'), 8)
print(len(ans))
"""
"""
def f(c, e, id_=""):
    if c > e or c in []: return 0
    if c == e: return 1
    if c < e:
        return f(c + 1, e, id_="id1") + f(c + 2, e, id_="id2") + \
               (f(c * 2, e, id_="id3") if id_ != "id3" else 0)


print(f(1, 15, ""))
"""
"""
def f(c, e, c_id=0):
    # Работать будет только со счётчиком (тк разные рекурсивные ветки), с айди - нет
    if c > e or c in []: return 0
    if c == e: return c_id==1
    if c < e:
        return f(c + 1, e, c_id) + f(c + 2, e, c_id) + f(c * 2, e, c_id+1)


print(f(2, 12))
"""
"""
def f(c, e, c_id=0):
    # Работать будет только со счётчиком (тк разные рекурсивные ветки), с айди - нет
    if c > e or c in []: return 0
    if c == e: return c_id <= 3
    if c < e:
        return f(c + 2, e, c_id) + f(c * 3, e, c_id + 1) + f(c * 5, e, c_id + 1)


print(f(2, 200))
"""
"""
from functools import lru_cache


@lru_cache()
def f(c, e, c_id=0):
    # Работать будет только со счётчиком в начале
    if c % 2: c_id += 1
    if c > e or c in [] or c_id > 1: return 0  # c_id > 1 позволяет ускорить за счет уменьшения рекусривных вызовов
    if c == e: return c_id == 1
    if c < e:
        return f(c + 1, e, c_id) + f(c + 2, e, c_id) + f(c * 2, e, c_id)


print(f(2, 40))
"""


def f(c, e, c_id=0):
    # Работать будет только со счётчиком в начале
    if c % 2 == 0: c_id += 1
    if c > e or c in [] or c_id > 6: return 0
    if c == e: return c_id == 6
    if c < e:
        return f(c + 1, e, c_id) + f(c + 3, e, c_id) + f(c + 5, e, c_id)


print(f(3, 25))




