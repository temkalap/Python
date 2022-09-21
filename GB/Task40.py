#Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
sqare = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True
while game_is_on:
    # Крестик - латинская буква X, нолик - латинская буква O
    # Ходы принимаются в формате [0][0] = "X" или [2][1] = "О"
    move = input()
    exec("sqare" + move)
    for row in sqare:
        print(row)

    reference_matrix = [
        sqare[0],
        sqare[1],
        sqare[2],
        [i[0] for i in sqare],
        [i[1] for i in sqare],
        [i[2] for i in sqare],
        [sqare[0][0], sqare[1][1], sqare[2][2]],
        [sqare[0][2], sqare[1][1], sqare[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Game over!")
            game_is_on = False
            break