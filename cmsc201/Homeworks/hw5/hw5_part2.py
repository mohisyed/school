"""
File:         hw5_part2.py
Author:       Mohiuddin Syed
Date:         10/15/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  creates a pascals triangle

"""

def pascal_level(a_list):
    """
    :param a_list: a list represents the previous level in the pascal's triangle construction
    :return: a new list with the previous elements summed
    """
    first_list = [1]    # starting 1

    for x in range(len(a_list)-1):     # the amount of triangles
        first_list.append(a_list[x] + a_list[x+1])    # a list + (alist + 1)
    first_list.append(1)  # the ending 1
    return first_list
    pass



if __name__ == '__main__':
    next_line = [1]
    for i in range(10):
        print(next_line)
        next_line = pascal_level(next_line)

    print(pascal_level([1, 2, 3, 4, 5]))
    print(pascal_level([1, 1, 2, 3, 5, 8]))
    print(pascal_level([1, 1, 2, 3, 5, 8, 13, 1]))
