from copy import deepcopy


# Finds the first empty Position in a given field.
# returns false if all Positions are filled.
def findEmptyPosition(field, emptyLocation):
    for row in range(9):
        for col in range(9):
            if (field[row][col] == 0):
                emptyLocation[0] = row
                emptyLocation[1] = col
                return True
    return False


# checks if a given number is already used in a given fields row.
def isNumberUsedInRow(field, row, numToTry):
    for i in range(9):
        if (field[row][i] == numToTry):
            return True
    return False


# checks if a given number is already used in a given fields column.
def isNumberUsedInColumn(field, col, numToTry):
    for i in range(9):
        if (field[i][col] == numToTry):
            return True
    return False


# checks if a given number is already used in a given fields sub Grid (e.g. 3x3).
def isNumberUsedInSubGrid(field, row, col, numToTry):
    for i in range(3):
        for j in range(3):
            if (field[i + row][j + col] == numToTry):
                return True
    return False


# checks if a given number is valid in a given Position
def isLocationSafe(field, row, col, numToTry):
    return not isNumberUsedInRow(field, row, numToTry) and not isNumberUsedInColumn(field, col, numToTry) and not isNumberUsedInSubGrid(field, row - row % 3, col - col % 3, numToTry)


def solve(field):
    emptyLocation = [0, 0]

    if (not findEmptyPosition(field, emptyLocation)):
        return True

    row = emptyLocation[0]
    col = emptyLocation[1]

    for numToTry in range(1, 10):
        if (isLocationSafe(field, row, col, numToTry)):
            field[row][col] = numToTry
            if (solve(field)):
                return True
            field[row][col] = 0
    return False


def print_grid(unfinishedField, field):
    for i in range(9):
        for j in range(9):
            if j % 3 == 0:
                print("|", end='')
            print(unfinishedField[i][j], end='')
        print(" | ", end='')
        for j in range(9):
            if j % 3 == 0:
                print("|", end='')
            print(field[i][j], end='')
        print('')


def getInput(url):
    file = open(url)
    lines = [line.rstrip('\n') for line in file]  # get all Grid rows as separate String
    field = []
    SIZE = 9
    for row in enumerate(lines):  # convert all strings to fieldays
        line = []
        for character in enumerate(row[1]):
            line.append(int(character[1]))
        field.append(line)
    return field


# field = getInput("C:\\Users\\knorbien\\Downloads\\Grid.txt")
field = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
         [9, 0, 0, 3, 0, 5, 0, 0, 1],
         [0, 0, 1, 8, 0, 6, 4, 0, 0],
         [0, 0, 8, 1, 0, 2, 9, 0, 0],
         [7, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 6, 7, 0, 8, 2, 0, 0],
         [0, 0, 2, 6, 0, 9, 5, 0, 0],
         [8, 0, 0, 2, 0, 3, 0, 0, 9],
         [0, 0, 5, 0, 1, 0, 3, 0, 0]]
unfinishedField = deepcopy(field)
if (solve(field)):
    print_grid(unfinishedField, field)
else:
    print("No solution")
