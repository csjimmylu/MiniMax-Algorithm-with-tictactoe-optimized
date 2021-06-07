import copy as cp
# NOTE use cp.deepcopy() so the temp variable isn't linked with the other

class Cell:
    def __init__(self, position, location, max_val, min_val):
        self.position = position
        self.location = location # NOTE this is a list, [0] is row info and [1] is col info
        self.min_val = min_val
        self.max_val = max_val

def generate_cells(board):
    uboard = cp.deepcopy(board)
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            if uboard[i][j] != 'X' and uboard[i][j] != 'O':
                uboard[i][j] = Cell(uboard[i][j], [i,j], 0, 0)
                uboard[i][j].max_val = max_val(board, [i, j])
                uboard[i][j].min_val = min_val(board, [i, j])
                # NOTE convert uboard[i][j] into list of maxval and minval from objects
                uboard[i][j] = [uboard[i][j].position, uboard[i][j].max_val, uboard[i][j].min_val]
    return uboard

def max_val(board, location): # NOTE only generates one max_val by a given location, not entire board
    maxval = 0
    if board[location[0]][location[1]] != 'O' and board[location[0]][location[1]] != 'X':
        maxval += check_horizontal(board, location[0], 'max') # need row
        maxval += check_vertical(board, location[1], 'max') # need column
        # NOTE diagonal check is splitted into left and right diagonal for convienence
        maxval += left_diagonal(board, location[0], location[1], 'max')
        maxval += right_diagonal(board, location[0], location[1], 'max')
    
    return maxval

def min_val(board, location):
    minval = 0
    if board[location[0]][location[1]] != 'O' and board[location[0]][location[1]] != 'X':
        minval -= check_horizontal(board, location[0], 'min')
        minval -= check_vertical(board, location[1], 'min')
        minval -= left_diagonal(board, location[0], location[1], 'min')
        minval -= right_diagonal(board, location[0], location[1], 'min')
    
    return minval

def check_horizontal(board, row, u_type):
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'

    v = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s row
        if board[row][i] != opposed:
            unfilled += 1
            if board[row][i] == sign:
                v += 1

    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def check_vertical(board, col, u_type):
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'

    v = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s column
        if board[i][col] != opposed:
            unfilled += 1
            if board[i][col] == sign:
                v += 1

    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def left_diagonal(board, row, col, u_type): # NOTE top_left to bottom_right diagonal check
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'
        
    v = 0
    unfilled = 0
    if row == col:
        for i in range(3):
            if board[i][i] != opposed:
                unfilled += 1
                if board[i][i] == sign:
                    v += 1

    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def right_diagonal(board, row, col, u_type):
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'

    v = 0
    unfilled = 0
    state = False
    for i in range(len(board)):
        if board[i][abs(i-2)] == board[row][col]:
            state = True
        if board[i][abs(i-2)] != opposed:
            unfilled += 1
            if board[i][abs(i-2)] == sign:
                v +=1
    
    if unfilled == 3 and state == True:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def dispUboard(uboard):
    print('\n')
    count = 0
    print("Utility Board:\n")
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            count += 1
            if uboard[i][j] == 'O' or uboard[i][j] == 'X':
                print('  ',uboard[i][j],end='     ')
            else:
                print(uboard[i][j],end='  ')
            if count%3 == 0:
                print('\n')