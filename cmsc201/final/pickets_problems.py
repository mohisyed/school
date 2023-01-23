"""
File:    pickets_problem.py
Author:  Mohiuddin Syed
Date:    12/15/20
Section: 24
E-mail:  msyed2@umbc.edu
Description:
    takes a two dimensional list and returns True or False depending on whether the board is "valid" or not.
"""


def pickets_problem(board):
    true_or_false = True  # final boolean flag
    indicies_list = []  # coordinates of the "P" points
    board_length = len(board)  # variable for length of the board

    for i in range(board_length):  # loop to find the picket in board
        for z in range(len(board[i])):
            if board[i][z] == "P":
                indicies_list.append([i, z])

    indicies_length = len(indicies_list)  # length of the indicies list

    for i in range(indicies_length):  # for loop to check conditions
        for z in range(indicies_length):
            if i != z and (indicies_list[z][1] - indicies_list[i][1] == indicies_list[z][0] - indicies_list[i][0]):       # i not z and if both points of indices equal each other
                if (indicies_list[i][0] - indicies_list[z][0] > 1) and (indicies_list[i][1] - indicies_list[z][1] > 1):         # if indicies list is greater than 1
                    true_or_false = False             # sets final condtion flag to False
            if i != z and (indicies_list[z][1] - indicies_list[i][1] == indicies_list[i][0] - indicies_list[z][0]):
                if (indicies_list[i][0] - indicies_list[z][0] > 1) and (indicies_list[i][1] - indicies_list[z][1] > 1):
                    true_or_false = False

    return true_or_false


random_list = [["S", "S", "S", "S", "S"], ["S", "P", "P", "S", "S"], ["P", "S", "S", "P", "S"],
               ["S", "S", "S", "P", "S"], ["S", "S", "S", "S", "S"]]

print(pickets_problem(random_list))
