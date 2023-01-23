"""
File:    nth_day.py
Author:  Mohi Syed
Date:    12/14/20
Section: 24
E-mail:  Msyed2@umbc.edu
Description:
  Calculates how many gifts the user inputed through the use of recusion
"""


def number_of_gifts(n):
    if n == 1:          # base case
        return 1
    else:
        nth_day_gift = (n * (n + 1)) / 2               # equation of gifts recieved on the current day D
        equation = nth_day_gift + number_of_gifts(n - 1)        # n - 1 to negate the current day equation
        return equation


if __name__ == '__main__':
    user_input = int(input(("How many days did you recieve gifts: ")))
    print(number_of_gifts(user_input))
