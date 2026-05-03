board = [" "] * 9

player = "X"

for i in range(9):
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

    move = int(input("Player X, enter (0-8): "))

    if board[move] == " ":
        board[move] = player
    else:
        print("Already filled")
        continue

    if (board[0]==board[1]==board[2]!=" " or
        board[3]==board[4]==board[5]!=" " or
        board[6]==board[7]==board[8]!=" " or
        board[0]==board[3]==board[6]!=" " or
        board[1]==board[4]==board[7]!=" " or
        board[2]==board[5]==board[8]!=" " or
        board[0]==board[4]==board[8]!=" " or
        board[2]==board[4]==board[6]!=" "):

        print("Player", player, "wins ")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    print("Match Tie ")