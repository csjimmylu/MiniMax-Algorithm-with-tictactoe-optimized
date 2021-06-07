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

    # TODO add the functions that generates min_val and max_val here
    return uboard

def check_MAX_horizontal(board, row):
    maxv = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s row
        if board[row][i] != 'X':
            unfilled += 1
            if board[row][i] == 'O':
                maxv += 1

    if unfilled == 3:
        if maxv == 2:
            maxv = 10
        else:
            maxv += 1
    elif unfilled < 3:
        maxv = 0

    return maxv

def check_MAX_vertical(board, col):
    maxv = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s column
        if board[i][col] != 'X':
            unfilled += 1
            if board[i][col] == 'O':
                maxv += 1

    if unfilled == 3:
        if maxv == 2:
            maxv = 10
        else:
            maxv += 1
    elif unfilled < 3:
        maxv = 0

    return maxv

def left_MAX_diagonal(board, row, col): # NOTE top_left to bottom_right diagonal check
    maxv = 0
    unfilled = 0
    if row == col:
        for i in range(3):
            if board[i][i] != 'X':

def right_MAX_diagonal(board, row, col):
    pass

def max_val(board, location): # NOTE only generates one max_val by a given location, not entire board
    maxval = 0
    if board[location[0]][location[1]] != 'O' and board[location[0]][location[1]] != 'X':
        # maxval += check_MAX_horizontal(board, location[0]) # need row
        # maxval += check_MAX_vertical(board, location[1]) # need column
        # # NOTE diagonal check splitted into left and right diagonal for convienence
        maxval += left_MAX_diagonal(board, location[0], location[1])
        # maxval += right_MAX_diagonal(board, location[0], location[1])
    
    return maxval

# NOTE below are test codes
# init_board = [[0, 'X', 2], 
#               ['O', 4, 'X'],
#               [6, 'O', 8]]

# val = max_val(init_board, [1,1])
# print(val)


def min_val(board, location):
    minval = 0
    if board[location[0]][location[1]] != 'O' and board[location[0]][location[1]] != 'X':
        check_MIN_horizontal()
        check_MIN_vertical()
        check_MIN_diagonal()
    pass




'''
board1 = [[0, 1, 'O'],
          [3, 'X', 5],
          ['X', 7, 8]]

utilityB = generate_cells(board1)
# print(utilityB)
for i in range(len(utilityB)):
    for j in range(len(utilityB[i])):
        if j == 0:
            print('')
        if utilityB[i][j] == 'X' or utilityB[i][j] == 'O':
            print(utilityB[i][j], end='    ')
        else:
            print(utilityB[i][j].position, end='    ')
'''