# Найти сумму чисел списка стоящих на нечетной позиции
List1 = [x for x in range(1, 10) if (not x % 2 == 0)]
print(List1)
print(sum(List1))
