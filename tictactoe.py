from minimax_utility_class import generate_cells
from minimax_utility_class import dispUboard
from MiniMax_Algorithm import minimax_algorithm

# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]


def checkWin(board, sign):
    if checkHorizontal(board, sign) == True:
        return True
    if checkVertical(board, sign) == True:
        return True
    if checkDiagonal(board, sign) == True:
        return True
    return False

def checkTie(board):
    filled = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O' or board[i][j] == 'X':
                filled += 1
    if filled == 9:
        return True
    return False

def checkDiagonal(board, sign):
    for i in range(len(board)):
        filled = 0
        if board[0][0] == sign:
            for j in range(len(board[i])):
                if board[j][j] == sign:
                    filled += 1
        elif board[0][2] == sign:
            for j in range(len(board[i])):
                if board[0+j][2-j] == sign:
                    filled += 1
    if filled == 3:
        return True
    return False

def checkHorizontal(board, sign): # NOTE BUGGY so fix it
    for i in range(len(board)):
        if board[i][0] == sign:
            filled = 0
            for j in range(len(board[i])):
                if board[i][j] == sign:
                    filled += 1
            if filled == 3:
                return True
    return False

def checkVertical(board, sign):
    for i in range(len(board)):  
        if board[0][i] == sign:
            filled = 0
            for j in range(len(board[i])):
                if board[j][i] == sign:
                    filled += 1
            if filled == 3:
                return True
    return False

def dispboard(board):
    print('\n')
    count = 0
    print('Tictactoe Board:\n')
    for i in range(len(board)):
        for j in range(len(board[i])):
            count += 1
            print(board[i][j],end='  ')
            if count%3 == 0:
                print('\n')

def checkCompatible(board, move, sign):
    i = 2
    if move <= 2:
        i = 0
    elif move >= 3 and move <= 5:
        i = 1
    
    loc = [i,(move-(i*3))]

    if board[loc[0]][loc[1]] == move:
        board[loc[0]][loc[1]] = sign
        return True
    else:
        print("Please select an empty spot and try again.")
        return False

def computerDecision(board):
    while (checkTie(board) == False) and (checkWin(board, 'X') == False):
        uboard = generate_cells(board)
        dispUboard(uboard)
        dispboard(board)

        # TODO run minimax algorithm here
        computer_decision = minimax_algorithm(uboard)
        computer_decision = int(computer_decision)

        if checkCompatible(board, computer_decision, 'O') == True:
            if checkTie(board) == True:
                dispboard(board)
                play_again = input("\nThis is a tie game, to play again enter any key, otherwise enter 'q' to quit.\nYour decision: ")
                if play_again == 'q':
                    return
                else:
                    board = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
                    GameInitializer(board)

            elif checkWin(board, 'O') == True:
                dispboard(board)
                print("The computer won!")
                return
            else:
                playerDecision(board)
        else:
            computerDecision(board)

def playerDecision(board):
    while (checkTie(board) == False) and (checkWin(board, 'O') == False):
        dispboard(board)
        player_decision = input("\n(The player's turn) Enter the empty position you want to place your 'X': ")
        player_decision = int(player_decision)

        if checkCompatible(board, player_decision, 'X') == True:
            if checkTie(board) == True:
                dispboard(board)
                play_again = input("\nThis is a tie game, if you want to play again enter 'p', to quit enter any key.\nYour decision: ")
                if play_again == 'q':
                    return
                else:
                    board = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
                    GameInitializer(board)

            elif checkWin(board, 'X') == True:
                dispboard(board)
                print("The player won!")
                return
            else:
                computerDecision(board)
        else:
            playerDecision(board)

def GameInitializer(board):
    choice = input("\nDo you want to go first or the computer goes first?\nEnter 'c' for computer first, or 'p' if you would like to go first\nYour Choice: ")
    if choice == 'c':
        computerDecision(board)
    elif choice == 'p':
        playerDecision(board)
    else:
        print("\nPlease enter 'c' or 'p' and try again.")
        GameInitializer(board)