"""
File:    how_deep.py
Author:  Mohiuddin Syed
Date:    4/15/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    uses recursion to find how many [] are in a function

"""

import random


def how_deep(list_struct):
    counter_depth = 0  # final counter variable
    for other_list in list_struct:  # sub list in the input
        depth = how_deep(other_list)
        if depth > counter_depth:  # recursion greater than counter variable
            counter_depth = depth  # its equal to it
    return 1 + counter_depth  # returns


def make_list_structure(max_depth, p=.8):
    if max_depth and random.random() < p:
        new_list = []
        for i in range(5):
            sub_list = make_list_structure(max_depth - 1, p * .9)
            if sub_list is not None:
                new_list.append(sub_list)
        return new_list
    return None


if __name__ == '__main__':
    print(how_deep([[[], [], [], [[[]]]], []]))
    print(how_deep([]))
    print(how_deep([[], []]))
    print(how_deep([[[]], [], [[]], [[[]]]]))
    print(how_deep([[[[], [[]], [[[]]], [[[[]]]]]]]))
    print(how_deep([[[], []], [], [[], []]]))
