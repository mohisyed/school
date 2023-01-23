"""
File:    lucky_base.py
Author:  Mohi Syed
Date:    12/15/20
Section: 24
E-mail:  Msyed2@umbc.edu
Description:
  takes an integer and returns a string which is that integer converted into base 7
"""


def lucky_base(number):
    empty_string = ""
    if number != 0:  # base case
        while number:  # loop till it hits 0
            empty_string = str(number % 7) + empty_string  # updates the empty string with a equation 
            number //= 7  # makes it sure its base 7
        return empty_string  # actually updates the string here
    else:
        return "0"  # if its zero will return zero


user_input = int(input("Enter a decimal number: "))
print(user_input, "to base 7 ", lucky_base(user_input))
