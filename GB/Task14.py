#Подсчитать сумму цифр в вещественном числе.
def GetNumberCount(number):
    numstr=str(number)
    count=0
    for i in numstr:
        if not i=='.':
            count+=1
    return count

print(GetNumberCount(100.233236))