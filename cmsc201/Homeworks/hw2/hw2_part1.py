"""
File:        hw2_part1.py
Author:      Mohiuddin Syed
Date:        9/15/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Tells the user whether or not they have enough ingredients to make
             Zucchini bread
"""

brown_sugar = int(input("How many cups of brown sugar do you have? "))
white_sugar = int(input("How many cups of brown sugar do you have? "))
egg = int(input("How many eggs do you have? "))
vegetable_oil = int(input("How many cups of vegetable oil? "))
flour_cups = int(input("How many cups of flour do you have? "))
zucchini = (input("Do you have a giant zucchni? (yes or no) "))

if brown_sugar <= 1:
    print("You do not have enough brown sugar.")
elif white_sugar <= 1:
    print("You do not have enough white sugar.")
elif egg <= 2:
    print("You do not have enough egg.")
elif vegetable_oil <= 1:
    print("You do not have enough vegetable oil.")
elif flour_cups <= 3:
    print("You do not have enough flour.")
elif zucchini != "yes" :
    print("You do not have enough zucchini.")
else:
    print("Your good to start cooking! ")
