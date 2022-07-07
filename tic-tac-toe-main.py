from copy import deepcopy
from time import sleep
import random as r

matrix = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def display_board(grid):
    '''Takes grid as input and returns void'''
    print(f'''
    -------------
    | {grid[0][0]} | {grid[0][1]} | {grid[0][2]} |
    -------------
    | {grid[1][0]} | {grid[1][1]} | {grid[1][2]} |
    -------------
    | {grid[2][0]} | {grid[2][1]} | {grid[2][2]} |
    -------------''')

def get_move(matrix):
    '''User Move Validation Returns Tuple'''
    while True:
        try:
            col,row = map(int,input('Enter your move in the format (col,row): ').lstrip('(').rstrip(')').split(','))
            assert row > 0 and row < 4
            assert col > 0 and row < 4
        except ValueError:
            print("Error: Coordinates must be two integer values")
        except AssertionError:
            print("Error: Coordinates must be within range 1-3 inclusive")
        else:
            if matrix[row - 1][col - 1] == ' ':
                break
            else:
                print('Error: Coordinates must be empty')
    return row, col

def winner_check(grid):
    '''Searches matrix for winner. Returns 1 if tie else winner str'''
    # Horizontal Match
    for i in range(3):
        if len(set(grid[i])) == 1 and ' ' not in grid[i]:
            return grid[i][0]
        
    # Vertical Match
    for i in range(3):
        column_data = set()
        for j in range(3):
            column_data.add(grid[j][i])
        if len(column_data) == 1 and ' ' not in column_data:
            return grid[0][i]
    # Diagonal Match
    top_left_diag, top_right_diag = set(), set()
    for i in range(3):
        top_left_diag.add(grid[i][i])
        top_right_diag.add(grid[i][-(i+1)])
    
    if (len(top_left_diag) == 1 or len(top_right_diag) == 1) and grid[1][1] != ' ':
        return grid[1][1]
    
    for row in grid:
        for item in row:
            if item == ' ':
                return None
    
    return 1

def computer_move(grid):
    '''Searches grid for possible winning moves for self and opponent else random'''
    for i in range(3):
        for j in range(3):
            grid_copy = deepcopy(grid)
            grid_copy[i][j] = 'O'
            if winner_check(grid_copy) == 'O' and grid[i][j] == ' ':
                return i, j

    for i in range(3):
        for j in range(3):
            grid_copy = deepcopy(grid)
            grid_copy[i][j] = 'X'
            if winner_check(grid_copy) == 'X' and grid[i][j] == ' ':
                return i, j

    row, col = r.randint(0, 2), r.randint(0, 2)
    
    while grid[row][col] != ' ':
        row, col = r.randint(0, 2), r.randint(0, 2)
    
    return row, col

for _ in range(9):
    row,col = get_move(matrix)
    matrix[row - 1][col - 1] = 'X'
    display_board(matrix)
    winner = winner_check(matrix)
    if winner in ['X','O']:
        print(f'{winner} wins!')
        break
    elif winner == 1:
        print("There was a tie!")
        break
    computer_row, computer_col = computer_move(matrix)
    matrix[computer_row][computer_col] = 'O'
    sleep(1)
    display_board(matrix)
    winner = winner_check(matrix)
    if winner in ['X','O']:
        print(f'{winner} wins!')
        break
    elif winner == 1:
        print("There was a tie!")
        break