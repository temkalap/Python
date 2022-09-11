# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
def get_sum(str1,str2):
    lst1=get_parsed_list(str1)
    lst2=get_parsed_list(str2)
    max_size=max(len(lst1),len(lst2))

    for i in range (0,max_size):
        if len(lst1)==max_size

def get_parsed_list(string):
    result_list = []
    lst = str(string).split('+')
    for item in lst:
        item_l = tuple(item.split('x^'))
        result_list.append(item_l)
    return normalise(result_list)


def normalise(lst):
    result_list = []
    for i in range(0,len(lst)+1):

        if i==len(lst)+1:
            continue
        if lst[i][2]==lst[i+1][2]+1:
            result_list.append(lst[i])
        else:
            result_list.append((0,lst[i][2]-1))
    return  result_list

str1 = ''
str2 = ''
with open('multipl1.txt', 'r') as file:
    str1 = file.read()
with open('multipl2.txt', 'r') as file:
    str2 = file.read()

print(str1)
print(str2)
