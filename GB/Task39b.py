import Task39a
from random import randint as randint
numsOfCandies = 2021
counter = 0

def pcTurn(numsOfCandies):
    takenCandies = randint(1, 28)
    while takenCandies > numsOfCandies:
        takenCandies = randint(1, 28)
    if numsOfCandies <= 28:
        takenCandies = numsOfCandies
    if 28 < numsOfCandies < 56:
        takenCandies = numsOfCandies - 29
    numsOfCandies -= takenCandies
    print(f'Бот забирает {takenCandies} конфет. Осталось конфет: {numsOfCandies}')
    return numsOfCandies

while numsOfCandies > 0:
        if numsOfCandies > 0:
            print('Ход игрока 1')
            numsOfCandies = Task39a.playerTurn(numsOfCandies)
            counter += 1
        if numsOfCandies > 0:
            print('Ход Бота')
            numsOfCandies = pcTurn(numsOfCandies)
            counter += 1
if counter % 2 == 0:
    print('Победил Бот')
else:
    print('Победил игрок')
