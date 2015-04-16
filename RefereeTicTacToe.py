"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who
marking the spaces in a 3x3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results.
You are given a result of a game and you must determine if the game ends in a win or a
draw as well as who will be the winner. Make sure to return "X" if the X-player wins
and "O" if the O-player wins. If the game is a draw, return "D".
"""


def referee_game(board):
    #horizontal
    for x, y in enumerate(board):
        if y.count(y[0]) == 3 and y[0] != '.':
            return y[0]


    #vertical
    first_row = board[0]
    for i, j in enumerate(first_row):
        count = 0
        ch = j
        if ch == '.':
            continue

        for x in range(0, 3):
            if board[x][i] == ch:
                count += 1

        if count == 3 and ch != '.':
            return ch



    #diagonal
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != '.':
        print True
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != '.':
        print True
        return board[0][2]

    return "D"

print referee_game(["X.O", "XX.","XOO"]) == "X"


print referee_game([
    "OO.",
    "XOX",
    "XOX"]) == "O"

print referee_game([
    "OOX",
    "XXO",
    "OXX"]) == "D"

print referee_game([
        "O.X",
        "XX.",
        "XOO"]) == "X"