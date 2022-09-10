# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
lst = [1.1, 1.2, 3.1, 5, 10.01]
lst1 = [str(x)[str(float(x)).find('.') + 1:] for x in lst]
lst2 = []
for i in range(0, len(lst1)):
    x = len(lst1[i])
    if len(lst1[i]) == 0:
        continue
    if lst1[i][0] == '0':
        lst1[i] = '0.' + lst1[i][1:]
    lst2.append(float(lst1[i]))

print(max(lst2) - min(lst2))
