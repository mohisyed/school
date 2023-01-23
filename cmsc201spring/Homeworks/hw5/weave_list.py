"""
File:    weave_list.py
Author:  Mohiuddin Syed
Date:    3/9/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    combines two list that the user inputs
"""
list_one_input = (input("First list: "))
list_one_input = list_one_input.split()

list_two_input = input("Second list: ")
list_two_input = list_two_input.split()

splitter_input = input("what charachther do you want to split with? ")

x = 0
y = []
if len(list_one_input) >= len(list_two_input):
    for i in range(len(list_one_input)):
        if len(list_two_input) >= i:
            y.append(list_one_input[i])
            y.append(splitter_input)
            y.append(list_two_input[i])
            y.append(splitter_input)
        elif len(list_two_input) < i:
            y.append(list_one_input[i])
            y.append(splitter_input)

elif len(list_one_input) <= len(list_two_input):
    for i in range(len(list_two_input)):
        if len(list_one_input) >= i:
            y.append(list_one_input[i])
            y.append(splitter_input)
            y.append(list_two_input[i])
            y.append(splitter_input)
        elif len(list_one_input) < i:
            y.append(list_two_input)
            y.append(splitter_input)
print("".join(y))

