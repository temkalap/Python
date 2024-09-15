# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]


def GetSum(listo):
    newlist = []
    for i in range(0, int(GetQtyIteration(listo))):
        newlist.append((listo[i] * listo[-i - 1]))
    return newlist


def GetQtyIteration(listo):
    if len(listo) % 2 == 0:
        return len(listo) / 2
    else:
        return len(listo) / 2 + 1


print(GetSum((list1)))
print(GetSum((list2)))
