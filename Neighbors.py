"""
You are given a state for a rectangular board game grid
with chips in a binary matrix, where 1 is a cell with a
chip and 0 is an empty cell. You are also given the coordinates for a cell in
the form of row and column numbers (starting from 0). You should determine how
many chips are close to this cell. Every cell interacts with its eight
neighbours; those cells that are horizontally, vertically, or diagonally adjacent.
For the given examples (see the schema) there is the same grid:

((1, 0, 0, 1, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)

For the first example coordinates of the cell is (1, 2) and as we can see from
the schema this cell has 3 neighbour chips. For the second example coordinates
is (0, 0) and this cell contains a chip, but we count only neighbours and the
answer is 1.
"""

def count_neighbors(grid, x, y):
    columns = len(grid)
    row = len(grid[0])
    beginCol = 0
    beginRow = 0
    currX = x
    currY = y
    counter = 0

    #go right
    if x + 1 < columns:
        currX = x + 1

        if grid[currX][y] == 1:
            counter = counter + 1

    #go left
    if x - 1 >= beginCol:
        currX = x - 1

        if grid[currX][y] == 1:
            counter = counter + 1

    #go up
    if y - 1 >= beginRow:
        currY = y - 1

        if grid[x][currY] == 1:
            counter = counter + 1

    #go down
    if y + 1 < row:
        currY = y + 1

        if grid[x][currY] == 1:
            counter = counter + 1


    #go diag bottom left
    if (y + 1 < row) and (x - 1 >= beginCol):
        currX = x - 1
        currY = y + 1

        if grid[currX][currY] == 1:
            counter = counter + 1

    #go diag bottom right
    if (y + 1 < row) and (x + 1 < columns):
        currX = x + 1
        currY = y + 1

        if grid[currX][currY] == 1:
            counter = counter + 1

    #go diag top left
    if (y - 1 >= beginRow) and (x - 1 >= beginCol):
        currX = x - 1
        currY = y - 1

        if grid[currX][currY] == 1:
            counter = counter + 1

    #go diag top right
    if (y - 1 >= beginRow) and (x + 1 < row):
        currX = x + 1
        currY = y - 1

        if grid[currX][currY] == 1:
            counter = counter + 1

    print counter
    return counter

print count_neighbors(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3

print count_neighbors(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1


print count_neighbors(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3


print count_neighbors(
    ((1,0,1,0,1),
     (0,1,0,1,0),
     (1,0,1,0,1),
     (0,1,0,1,0),
     (1,0,1,0,1),
     (0,1,0,1,0),), 5, 4)