"""
File:    binary_choice.py
Author:  Mohiuddin Syed
Date:    4/13/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    prints out binary sequence 

"""


def a_binary_choice(n, k, current=''):
    """
    prints out all sequences of 0's and 1's of length n that have exactly k 1's.
    : param n: an integer
    """
    if n == 0:  #
        if k == 0:
            print(current)
        return
    if k > 0:
        a_binary_choice(n - 1, k - 1, current + "1")  # add 1 and recalls the function
    a_binary_choice(n - 1, k, current + "0")  # add 0 and recalls the function


if __name__ == '__main__':
    a_binary_choice(6, 3)
    a_binary_choice(4, 2)
