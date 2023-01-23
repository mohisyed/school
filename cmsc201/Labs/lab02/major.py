"""
File:         major.py
Author:       Mohiuddin Syed
Date:         2/17/2018
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Checks what grade you need to get in order to see if the class
              will count for you.
"""

user_input = input("Please enter your major: ")

if user_input == "CMSC" or user_input== "CMPE":
    print("you need to earn at least a B for CMSC 201 to count")
else:
    print("you need to earn at least a C for CMSC 201 to count")
