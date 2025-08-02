def del_(num1, num2):
    return num1 % num2 == 0


def f(x, a):
    return (del_(x, 3) <= (not del_(x, 5))) or (x + a >= 90)


for a_ in range(1, 1000):
    if all([f(x, a_) for x in range(1, 3000)]):
        print(a_)
        break