"""
File:         hw4_part3.py
Author:       Mohiuddin Syed
Date:         10/1/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Creates a pattern board. user chooses the size
"""
if __name__ == "__main__":
    pattern_list = ['\u2660', '\u2665', '\u2666', '\u2663']  # pattern list 
    user_input = int(input("What size board do you want? "))
    row = user_input       # just the size of the row
    column = user_input    # just the size of the column
    for x in range(row):    
        for y in range(column):
            check = ((y + x) % 4) # checks when x and y is greater than 8. returns value back to 0-3
            if check == 0:         
                print(pattern_list[0], end=" ")       # creates pattern starting from 0 (first row)
            if check == 1:
                print(pattern_list[1], end=" ")       # creates pattern starting from 1 (second row)
            if check == 2:
                print(pattern_list[2], end=" ")       # creates pattern starting from 2 (third row)
            if check == 3:
                print(pattern_list[3], end=" ")       # creates pattern starting from 3 (fourth row)
        print()      # line break makes it a square 






