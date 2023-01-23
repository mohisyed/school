"""
File:    Junble.py
Author:  Mohi Syed
Date:    12/15/20
Section: 24
E-mail:  Msyed2@umbc.edu
Description:
    jumbles the user inputs 
"""

def jumble(astring,a ,b):
    L = len(astring)
    final_word_list = []
    some_string = ""
    for i in range(L):
        formula = (a * i + b) % len(astring)    # the formula
        if formula not in final_word_list:        
            final_word_list.append(formula)      # appends to the list
            some_string += astring[formula]     # adds it to the string 
    return some_string



if __name__ == '__main__':
    print("The equation: ax + b % l")
    a_input = int(input("what will a be? "))
    b_input = int(input("what will b be? "))
    string_input = input('what will the word be? ')

    jumble(string_input, a_input, b_input)
    jumble("diwdiwdiw", 3, 7)
