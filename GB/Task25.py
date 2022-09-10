# Написать программу преобразования десятичного числа в двоичное
def tenToTwise(x):
    stri = ''
    while x > 0:
        stri = str(x % 2) + stri
        x = x // 2
    return stri


print(tenToTwise(29))
