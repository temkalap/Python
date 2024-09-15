# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
def getFibonacci(n):
    k = 1
    if n < 0:
        k = -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return k * getFibonacci(n - 1 * k) + getFibonacci(n - 2 * k)


lst = []
n = 10
for i in range(-n, n + 1):
    lst.append(getFibonacci(i))

print(lst)
