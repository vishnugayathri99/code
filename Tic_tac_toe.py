import random,sys,time
n=[j for j in range(1,10)]
board=[" "for i in range(9)]
print("TIC-TAC-TOE")
print()
def print_board():
    row1="| {} | {} | {} |".format(board[0],board[1],board[2])
    row2="| {} | {} | {} |".format(board[3],board[4],board[5])
    row3="| {} | {} | {} |".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
def player_move(icon):
    if icon=="X":
        number=1
    elif icon=="O":
        number=2
    print("Your turn player {}".format(number))
    choice1=int(input("Enter your move (1-9):").strip())
    if choice1>0 and choice1<=9:
        if board[choice1-1]==" ":
            board[choice1-1]=icon
        else:
            print()
            print("The space was taken.....:(")
            print()
            player_move(icon)
    else:
        print("invalid move...please enter again")
        player_move(icon)
def player_movec(icon):
    n1=random.choice(n)
    print("Computer turn :")
    time.sleep(0.5)
    print(n1)
    time.sleep(1)
    if board[n1-1]==" ":
        board[n1-1]=icon
    else:
        print("The space was taken.....:")
        print()
        player_movec(icon)
def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]== icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return  False
while True:
    ch=int(input("Which mode do you want to play \n 1.Computer vs Player\n 2. Player vs Player \n choice : "))
    if ch==1:
        while True:
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("Player(X) wins......Congratulations ")
                sys.exit()
            elif is_draw():
                print("It's a draw ")
                sys.exit()
            player_movec("O")

            if is_victory("O"):
                print_board()
                print("Player(O) wins......Congratulations ")
                sys.exit()
            elif is_draw():
                print("It's a draw ")
                sys.exit()
    elif ch==2:
        while True:
            print_board()
            player_move("X")
            print_board()
            if is_victory("X"):
                print("Player(X) wins......Congratulations ")
                sys.exit()
            elif is_draw():
                print("It's a draw ")
                sys.exit()
            player_move("O")
            if is_victory("O"):
                print_board()
                print("Player(O) wins......Congratulations ")
                sys.exit()
            elif is_draw():
                print("It's a draw ")
                sys.exit()
    else:
        print("Enter again:")
