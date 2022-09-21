# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

from random import randint as randint
numsOfCandies = 2021
counter = 0
def playerTurn(numsOfCandies):
    if numsOfCandies == 0:
        return -1
    takenCandies = int(input("Введите сколько конфет вы забираете: "))
    while takenCandies <= 0 or takenCandies > 28:
        takenCandies = int(input('Брать можно только от 1 до 28 конфет. Попробуйте снова: '))
        if numsOfCandies < takenCandies:
             print(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}')
    if numsOfCandies < takenCandies:
        while takenCandies <= 0 or takenCandies > numsOfCandies:
            takenCandies = int(input(f'осталось {numsOfCandies} конфет, введите число от 1 до {numsOfCandies}: '))
    numsOfCandies -= takenCandies
    return numsOfCandies

while numsOfCandies > 0:
       if numsOfCandies > 0:
           print('Ход игрока 1')
           numsOfCandies = playerTurn(numsOfCandies)
           counter += 1
       if numsOfCandies > 0:
           print('Ход игрока 2')
           numsOfCandies = playerTurn(numsOfCandies)
           counter += 1
if counter % 2 == 0:
   print('Победил игрок 2')
else:
   print('Победил игрок 1')