"""
File:         Knights_move_sum.py
Author:       Mohiuddin Syed
Date:         10/7/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  see all the possible knight moves
"""


import sys
from random import randint, seed

if len(sys.argv) >= 2:
   seed(sys.argv[1])

if __name__ == "__main__":
    the_matrix = []
    the_matrix = [[randint(0, 100) for j in range(4)] for i in range(4)]

    for i in range(4):
        new_row = []
        for j in range(4):
            new_row.append(randint(0, 100))
        the_matrix.append(new_row)

    row = int(input("What is the row that you want to start at? "))
    column = int(input("What is the column that you want to start at?"))

    counter = 0

    # didnt have enough time but u make boundaries here and define them
    # use the counter to add the numbers on the board
    # and u make a for loop to print matrix


