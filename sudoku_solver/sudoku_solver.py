# random board generator: https://www.sudokuweb.org/


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
