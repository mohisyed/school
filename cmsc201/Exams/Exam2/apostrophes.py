"""
File:    norgardSequence.py
Author:  Mohiuddin Syed
Date:    11/22/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: calculates the norgrad sequence
"""
def apostrophes(string):
    index = 0
    length = len(string)
    if string == 0:
        return ""
    else:
        if length == (index + 1):
            if string[index] == 's':
                string = string[:index] + "'" + string[index:]
            print(string)
            return ""
        else:
            if string[index] == 's' and not (string[index + 1].isalnum()):
                string = string[:index] + "'" + string[index:]
                

            apostrophes(string)


print("Enter the string")
string = str(input())

apostrophes(string)
