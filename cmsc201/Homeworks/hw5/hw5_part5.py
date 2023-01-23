
"""
File:         hw5_part5.py
Author:       Mohiuddin Syed
Date:         10/15/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Swap the max number in a list and put it to the back

"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

# USE IF YOU ARE TESTING AND DON'T WANT TO USE COMMAND LINE ARGUMENTS
# seed(input('What seed do you want to use? '))
# END SECTION

STOP_PARAM = 'STOP'
MAX_INT = 100
"""
    Start coding here! 
"""


def swap(the_list, i, j):
    """
    :param the_list: the list that we're reverse sorting
    :param i: the first position to swap
    :param j: the second position to swap
    """
    sub = the_list[i]  # substitution variable = the first position
    the_list[i] = the_list[j]  # swap the first with the second making a hard copy
    the_list[j] = sub  # substition variable = last position
    return the_list


def find_max_index_after(i, the_list):
    """
    :param i: start at position i to look for the max
    :param the_list: the list to search
    :return: the INDEX of the maximum, not the maximum itself!
    """
    negative_index_checker = -1
    counter = 0
    for v in range(i, len(the_list)):  # checking the i with length of the list
        if the_list[v] > negative_index_checker:  # if greater than neg index then replace it
            negative_index_checker = the_list[v]
            counter = v
    return v


def reverse_selection_sort(the_list):
    """
    :param the_list: the list to reverse sort
    :return: the reverse sorted list
    """
        for i in range(len(the_list)):
        final_counter = the_list
        final_index = find_max_index_after(i, the_list)
        final_counter = swap(final_counter, i, final_index)

    return final_counter


"""
    Your code should end here.  The driver below should not be modified during submission.  
"""


if __name__ == '__main__':
    length_or_stop = input('What length of list do you want to sort? (or STOP to end)')
    while length_or_stop != STOP_PARAM:
        try:
            the_list = [randint(0, MAX_INT) for _ in range(int(length_or_stop))]
            print('The list is: ', the_list)
            print('The reverse sort is: ', reverse_selection_sort(the_list))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input('What length of list do you want to sort? (or STOP to end)')
