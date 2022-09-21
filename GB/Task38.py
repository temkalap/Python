# Напишите программу, удаляющую из текста все слова содержащие "абв".
str1= 'абв проллджо выаолдпрлабв ввофцлдвпн'
lst1 = str1.split(' ')
str2 = [lst1[x] for x in range(len(lst1)) if not lst1[x].__contains__("абв")]
strResult = ''
for i in str2:
    strResult += i + ' '
print(strResult.strip())