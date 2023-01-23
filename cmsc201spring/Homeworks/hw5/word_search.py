"""
File:    word_search.py
Author:  Mohiuddin Syed
Date:    3/9/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    finds the wrd the user inputs in a jumbled string
"""


intial_input = input("Enter the block of characters to search: ").lower()
look_word_input = input("What is the word we are looking for? ").lower()
look_word_input = list(look_word_input)

final = []
offset = 0  # maybe a list
gap = 0

for i in range(len(intial_input)):
    if intial_input[i] == look_word_input:
        final.append(look_word_input[0])
        offset = i
    for x in range(offset + 1, len(intial_input)):
        if intial_input[x] == look_word_input[1]:
            if gap == 0:
                gap = x - offset
            



print(offset, gap)

