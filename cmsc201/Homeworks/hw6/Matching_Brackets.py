"""
File:    Matching_Brackets.py
Author:  Mohiuddin Syed
Date:    10/6/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: Tells the user wheither or not their input is valid or not.
"""


def match_brackets(bracket_string, count=0):
    if bracket_string == "":     # empty string
        if count != 0:
            return False
        else:
            return True
    else:
        if bracket_string[0] == "{":    # if open bracket (start)
            return match_brackets(bracket_string[1:], count + 1)
        if bracket_string[0] == "}":    # if close bracket (close)
            return match_brackets(bracket_string[1:], count - 1)
        else:
            return match_brackets(bracket_string[1:], count)


if __name__ == "__main__":
    t_f = True
    while t_f:
        bracket = input("enter a string with brackets: ")
        if bracket.lower() == "quit":
            t_f = False
        else:
            print(match_brackets(bracket))
