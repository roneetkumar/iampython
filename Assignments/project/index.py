from math import ceil
from random import randint

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

rows = len(grid)
cols = len(grid[0])

x, y = ceil(rows/2)-1, ceil(cols/2)-1

grid[x][y] = 1

for row in grid:
    for i in row:
        print(f"{i} ", end='')
    print("")

# 1 = l
# 2 = r
# 3 = t
# 4 = b


def walk(x, y):
    pos = randint(1, 4)
    if str(pos) == '1':
        y -= 1
        print('Move Left\n')
    elif str(pos) == '2':
        y += 1
        print('Move Right\n')
    elif str(pos) == '3':
        x -= 1
        print('Move Up\n')
    elif str(pos) == '4':
        x += 1
        print('Move Down\n')
    if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
        print('exit')
        return

    grid[x][y] += 1

    for row in grid:
        for i in row:
            print(f"{i} ", end='')
        print("")

    walk(x, y)


walk(x, y)
