import numpy
def islandPerimeter(grid):
    a = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                a += 4

                try:
                    if j < (len(grid[0]) - 1) and grid[i][j + 1] == 1:
                       a -= 1
                except :
                    pass

                try:
                    if j > 0 and grid[i][j - 1] == 1:
                        a -= 1
                except :
                    pass

                try:
                    if i < (len(grid) - 1) and grid[i + 1][j] == 1:
                        a -= 1
                except :
                    pass

                try:
                    if i > 0 and grid[i - 1][j] == 1:
                        a -= 1
                except :
                    pass


    return a

if __name__ == '__main__':
    grid = [[0,1,0,0],            [1,1,1,0],            [0,1,0,0],            [1,1,0,0]]
    grid = numpy.array(grid)
    print grid


    print islandPerimeter(grid)