def build_grid():
    f = open("input.txt", "r")
    grid = []
    for i in f.readlines():
        grid.append([str(j) for j in i.strip("\n")])
    return grid

def get_path(x_step, y_step):
    grid = build_grid()
    path = []
    x = 0
    y = 0
    while y < len(grid):
        looped_x = x % len(grid[y])
        path.append(grid[y][looped_x])
        y += y_step
        x += x_step
    return path

def puzzle_1():
    print(get_path(3, 1).count("#"))

def puzzle_2():
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    # must be 1, or multiplication will be weird
    total = 1
    for i in slopes:
        total = total * get_path(i[0], i[1]).count("#")
    print(total)

puzzle_2()