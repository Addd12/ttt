import math
import copy

X = "X"
O = "O"
EMPTY = None

grid = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
# store all the possible moves on a set
def actions(grid):
    moves = set()

    for i in range(3):
        for j in range(3):
            if grid[i][j] == EMPTY:
                moves.add((i, j))

    return moves

def player(grid):
    x_number = 0
    O_number = 0

    for i in range(3):
        for j in range(3):
            if grid[i][j] == X:
                x_number += 1
            elif grid[i][j] == O:
                O_number += 1
    # switch player
    if x_number > O_number:
        return O
    else:
        return X

def result(grid, action):
    # Create new board, from the current input
    new_board = copy.deepcopy(grid)
    new_board[action[0]][action[1]] = player(grid)
    return new_board
# check for winner
def winner(grid):
    # check columns
    col_1 = grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] != None
    col_2 = grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] != None
    col_3 = grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] != None
    # check rows 
    row_1 = grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] != None
    row_2 = grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] != None
    row_3 = grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] != None
    # check diagonals
    dgn_1 = grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] != None
    dgn_2 = grid[2][0] == grid[1][1] and grid[1][1] == grid[0][2] != None

    if col_1:
        if grid[0][0] == X:
            return X
        else:
            return O
    elif col_2:
        if grid[1][0] == X:
            return X
        else:
            return O
    elif col_3:
        if grid[2][0] == X:
            return X
        else:
            return O
    elif row_1:
        if grid[0][0] == X:
            return X
        else:
            return O
    elif row_2:
        if grid[0][1] == X:
            return X
        else:
            return O
    elif row_3:
        if grid[0][2] == X:
            return X
        else:
            return O
    elif dgn_1:
        if grid[0][0] == X:
            return X
        else:
            return O
    elif dgn_2:
        if grid[2][0] == X:
            return X
        else:
            return O
    else:
        return None 
# check if gthe game is over
def terminal(grid):

    if winner(grid) == X or winner(grid) == O:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if  grid[i][j] == None:
                    return False
                    
    return True
# assign values to each possible case
def utility(grid):
    if terminal(grid):
        if winner(grid) == X:
            return 1
        elif winner(grid) == O:
            return -1
        else:
            return 0

def minimax(grid):
    if terminal(grid):
        return None
    else:
        if player(grid) == X:
            value, move = maximize(grid)
            return move
        else:
            value, move = minimize(grid)
            return move

# try to maximize value
def maximize(grid):
    if terminal(grid):
        return [utility(grid), None]
    # initially assign the lowest value
    value = float('-inf')
    move = None
    for action in actions(grid):
        x, y = minimize(result(grid, action))
        if x > value:
            # if there's a bigger value, assign it as the new value
            value = x
            move = action
            if value == 1:
                return value, move

    return value, move

# try to minimize value
def minimize(grid):
    if terminal(grid):
        return [utility(grid), None]
    # initially assign the biggest value
    value = float('inf')
    move = None
    for action in actions(grid):
        x, y = maximize(result(grid, action))
        if x < value:
            # if there's a smaller value, assign it as the new value
            value = x
            move = action
            if value == -1:
                return value, move

    return value, move
