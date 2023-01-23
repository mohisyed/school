"""
File:    norgardSequence.py
Author:  Mohiuddin Syed
Date:    11/22/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: calculates the norgrad sequence
"""


def norgrad_sequence(n):
    if n == 0:
        return 0

    if n % 2 == 0:
        return -norgrad_sequence(int(n/2))
    else:
        return norgrad_sequence(int(n)/2) + 1

if __name__ == '__main__':
    user_input = int(input("What do u want to calculate: "))
    if user_input < 0:
        print("enter a postive value: ")
    else:
        print(norgrad_sequence(user_input))
