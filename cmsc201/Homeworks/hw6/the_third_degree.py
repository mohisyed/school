"""
File:    the_third_degree.py
Author:  Mohiuddin Syed
Date:    10/6/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: Prints out a recursive formula
"""


def the_third_degree(n):
    if n in [0, 1, 2]:
        if n == 0:    # n term = 0
            return 2
        if n == 1:    # n term = 1
            return 1
        if n == 2:    # n term = 2
            return 5
    elif n > 2:    # n term > 2
        return 3 * the_third_degree((n - 1)) + 2 * the_third_degree((n - 2)) + the_third_degree((n - 3))


if __name__ == '__main__':
    for i in range(10):
        print(the_third_degree(i))
