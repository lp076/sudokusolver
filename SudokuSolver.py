board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

#Finds an empty cell with value 0 and fetches its co-ordinates
def getEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
                #row, col format
    return None

#Sets the value of current working cell to digits 1-9 and checks if valid using isValidDigit function
def solve(board):
    #Gets and empty cell and assigns co-ordinates to "coordinates" variable, if no cell is found, the grid should have been solved
    coordinates = getEmptyCell(board)
    if not coordinates:
        return True

    row, col = coordinates[0], coordinates[1]

    for i in range(1, 10):
        if isValid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False

#Checks the row for any cells that may already contain the digit "num" at the cell's position "pos"
def checkRow(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    return True

#Checks columns for any cells that already contain the digit "num" at position "pos"
def checkColumns(board, num, pos):
    for i in range(len(board[0])):

        #where board[i] is y and pos[1] is x
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    return True

def checkBoxes(board, num, pos):
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #multiply by 3 to determine bottom bound, and add 3 to determine top bound
    #example: box 2 on a normal sudoku grid indexes at box 1, therefore if we multiply by 3, we have a range of (4,7) which are all of the cells
    #contained within box 2
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

#Checks if "num" is valid using the 3 helper functions above.
def isValid(board, num, pos):
    if checkRow(board, num, pos):
        if checkColumns(board, num, pos):
            if checkBoxes(board, num, pos):
                return True
    return False

#Prints the board
def printBoard(board):
    for i in range(len(board)):
        #so that there is no line generated at the top of the board, we add i!=0
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        #so that there are no end caps on the board we add j!=0
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

printBoard(board)
solve(board)
print("\n \n")
printBoard(board)