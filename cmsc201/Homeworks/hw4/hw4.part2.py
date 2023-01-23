"""
File:         hw4_part2.py
Author:       Mohiuddin Syed
Date:         10/2/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Caeser salad cipher calculator. Can deciper the user inputs input
"""
if __name__ == "__main__":

    string_input = input("What is the string to encrypt? (or stop) ")
    final_string_input = ""
    length = len(string_input)   # constant for the length of string input

    if string_input != "stop":
        offset_input = int(input("What is the offset? "))
        for x in range(length):
            ascii_numb = ord(string_input[x])        # variable for ord string input easy to call in for
            if 65 <= ascii_numb <= 90:
                temp_ascii_numb = (ascii_numb) - 65         # temp variable to convert
                temp_ascii_numb = (temp_ascii_numb + offset_input + (x**2)) % 26       # equation of the sequence
                final_string_input += chr(temp_ascii_numb + 65)      # final anwser converts to string
            elif 97 <= ascii_numb <= 122:
                temp2_ascii_numb = (ascii_numb) - 97
                temp2_ascii_numb = (temp2_ascii_numb + offset_input + (x ** 2)) % 26
                final_string_input += chr(temp2_ascii_numb + 97)

    print("The encrypted string is , {}".format(final_string_input))
