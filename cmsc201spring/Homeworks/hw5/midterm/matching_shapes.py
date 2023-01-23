"""
File:    matching_shapes.py
Author:  Mohiuddin Syed
Date:    3/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
figures out if new shape can fit in the grid

"""


def is_there_space(grid, shape):
    checker = True
    if len(grid[0]) == len(shape[0]):
        for i in range(len(grid)):
            for x in range(len(grid[i])):
                if grid[i][x] == "" and shape[0][x] == "x":     # all the conditions to see if it fits in the space
                    checker = True

                elif grid[i][x] == "" and shape[1][x] == "x":
                    checker = True

                elif grid[i][x] == "x" and shape[0][x] == "":
                    checker = True

                elif grid[i][x] == "x" and shape[1][x] == "":
                    checker = True

                elif grid[i][x] == "x" and shape[0][x] == "x":
                    checker = False
                    return checker

                elif grid[i][x] == "x" and shape[1][x] == "x":
                    checker = False
                    return checker
    else:
        for i in range(len(grid)):
            for x in range(len(grid[i])):
                if grid[i][x] == "" and shape[0][x - 3] == "x":
                    checker = True

                elif grid[i][x] == "" and shape[1][x - 3] == "x":
                    checker = True

                elif grid[i][x] == "x" and shape[0][x - 3] == "":
                    checker = True

                elif grid[i][x] == "x" and shape[1][x - 3] == "":
                    checker = True

                elif grid[i][x] == "x" and shape[0][x - 3] == "x":
                    checker = False
                    return checker

                elif grid[i][x] == "x" and shape[1][x - 3] == "x":
                    checker = False
                    return checker

    return checker


if __name__ == "__main__":
    new_shape = [['', 'x', ''], ['x', 'x', 'x']]

    print(is_there_space([['x', 'x', 'x'],
                          ['x', 'x', 'x'],
                          ['x', 'x', 'x']],
                         new_shape))

    print(is_there_space([['x', 'x', 'x'],
                          ['x', '', 'x'],
                          ['x', 'x', 'x']],
                         new_shape))

    print(is_there_space([['x', 'x', ''],
                          ['x', '', ''],
                          ['x', '', '']],
                         new_shape))

    print(is_there_space([['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['x', '', '', '', ''],
                          ['x', '', '', '', ''],
                          ['x', '', '', '', '']],
                         new_shape))

