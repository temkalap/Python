# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
def get_sum(str1, str2):
    lst1 = get_parsed_list(str1)
    lst2 = get_parsed_list(str2)
    result_list = []
    max_size = max(len(lst1), len(lst2))
    min_size = min(len(lst1), len(lst2))
    for i in range(max_size - 1, 0, -1):
        j = max_size - min_size
        if len(lst1) == max_size:
            if lst1[i][1] == lst2[i][1]:
                result_list.append((lst1[i][0] + lst2[i][0], lst1[i][1]))
            else:
                result_list.append(lst1[i])
        else:
            if lst1[i][1] == lst2[i][1]:
                result_list.append((lst1[i][0] + lst2[i][0], lst1[i][1]))
            else:
                result_list.append(lst2[i])
    return result_list


def get_parsed_list(string):
    result_list = []
    lst = str(string).split('+')
    for item in lst:
        item_l = item.split('x^')
        for i in range(0, len(item_l)):
            item_l[i] = int(item_l[i])
        result_list.append(item_l)
    return normalise(result_list)


def normalise(lst):
    result_list = []
    for i in range(0, len(lst)):

        if i == len(lst) - 1:
            result_list.append(lst[i])
            break
        if lst[i][1] == lst[i + 1][1] + 1:
            result_list.append(lst[i])
        else:
            result_list.append([0, lst[i][1] - 1])
    return result_list


str1 = ''
str2 = ''
with open('multipl1.txt', 'r') as file:
    str1 = file.read().replace('=0', '')
with open('multipl2.txt', 'r') as file:
    str2 = file.read().replace('=0', '')

lst = get_sum(str1, str2)
print(lst)
