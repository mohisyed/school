# File:    hailstone.py
# Started: by Dr. Gibson
# Author:  Mohiuddin Syed
# Date:    5/12/21
# Section: 31
# E-mail:  msyed2@umbc.edu
# Description:
#   This file contains python code that implements the
#   "flight" of a hailstone, following the HOTPO rules
#   (also known as the Collatz Conjecture), recursively

# NO CONSTANTS NEEDED, THE NUMBERS USED IN flight() ARE
#    PART OF A FORMULA/MATHEMATICAL CONJECTURE

############################################################
# flight() recursively calculates the path of a hailstone
# Input:   the height of the hailstone
# Output:  a recursive call, which at the end returns
#          the number of "steps" taken for the
#          hailstone to reach a height of 1
def flight(height):
    #### BASE CASES:
    # if height is zero or lower, print out an "invalid" message and return 0
    print(height)
    if height <= 0:
        print("Invalid")
        return 0
    elif height == 1:
        return 0
    else:
        if height % 2 == 0:
            return flight(height / 2) + 1
        elif height % 2 == 1:
            return flight(height / 3) + 1
        # stops when it reaches height of 1 (the ground)

    #### RECURSIVE CASES:
    # if the current height is even, divide it by 2

    # if the current height is odd, multiply it by 3, then add 1


def main():
    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    startHeight = int(input(msg))
    steps = flight(startHeight)


    # recursive call goes here



    print("\nIt took", steps, "steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!\n")


main()
