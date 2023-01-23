"""
File:    alternating_sequence.py
Author:  Mohiuddin Syed
Date:    4/16/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    prints out the alternating sequence

"""


def alternating_sequence(n):
    if n in [0, 1, 2]:
        if n == 0:    # n term = 0
            return 2
        if n == 1:    # n term = 1
            return 3
        if n == 2:    # n term = 2
            return 4
    elif n > 2:    # n term > 2
        return 2 * alternating_sequence((n - 1)) - alternating_sequence((n - 2)) + alternating_sequence((n - 3))


if __name__ == '__main__':
    for i in range(10):
        print(i, alternating_sequence(i))
