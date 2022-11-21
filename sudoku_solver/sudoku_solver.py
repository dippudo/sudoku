# random board generator: https://www.sudokuweb.org/
# tutorial part 1: https://www.youtube.com/watch?v=eqUwSA0xI-s


# row = sub-list, column = item in sub-list
board = [
    [0, 0, 6, 7, 0, 0, 4, 0, 5],
    [0, 0, 0, 0, 0, 0 ,0 ,0, 6],
    [0, 0, 2, 6, 0, 0, 1, 0, 3],
    [0, 3, 4, 0, 1, 0, 6, 2, 0],
    [2, 0, 0, 3, 4, 0, 0, 5, 7],
    [9, 0, 5, 0, 6, 7, 3, 0, 0],
    [1, 5, 0, 0, 3, 0, 9, 6, 0],
    [6, 2, 3, 0, 5, 4, 7, 1, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


def print_board(board):
    # centre the title "SUDOKU" above the board
    spaces = 31 - int(len("SUDOKU"))
    print(r" " * int((int(spaces) / 2)) + r" " + "SUDOKU")

    for row in range(len(board)):
        # print separator before board
        if row == 0:
            print("+" + "-" * 29 + "+")
        # print separator every third row
        if row % 3 == 0 and row != 0:
            print("+" + "-" * 29 + "+")
    

        for column in range(len(board[0])):
            # print separator every every third column
            if column % 3 == 0 and column != 0:
                print(r" |  ", end="") # end="" makes python end the loop on the same line instead of automatically starting on a new line - by identifying the ending character with an empy character instead of newline

            # print separator before first column
            if column == 0:
                print(r"|  " + str(board[row][column]) + " ", end="")
            
            # print separator after last column
            elif column == 8:
                print(str(board[row][column]) + r"  |")
            
            # print the integer with spaces in between if not first or last row/column, then identifies end character as empty character instead of newline
            else:
                print(str(board[row][column]) + " ", end="")

    print("+" + "-" * 29 + "+")


# find an empty square
def find_empty(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return (row, column)

    return None


def valid(board, number, position):
    # check row
    for i in range(len(board[0])): # loop through rows (we are getting the length of a row through len(board[0]))
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(board)): # loop through columns (length of column == len(2dArray board))
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check 3x3 box
    box_row = position[1] // 3 # column index // 3
    box_column = position[0] // 3 # row index // 3

    for row in range(box_column * 3, box_column * 3 + 3):
        for column in range(box_row * 3, box_row * 3 + 3):
            if board[row][column] == number and (row, column) != position:
                return False

    return True


def solve(board): # updates board to the solved board
    find = find_empty(board)

    if not find: # if program cannot find an empty square
        return True # solve = True / THE BOARD HAS BEEN SOLVED

    else:
        row, column = find # return the coordinates of the empty square, if found

    for i in range(1, 10): # try every number between 1-9 inclusive
        if valid(board, i, (row, column)):
            board[row][column] = i # assign i to current empty square

            if solve(board): # recursively try to solve the board, using the above valid() function call
                return True

            board[row][column] = 0 # reset the previously solved square to 0 if no answers are found

    return False
