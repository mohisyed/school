"""
File:        hw2_part2.py
Author:      Mohiuddin Syed
Date:        9/16/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Allows the user to solve the puzzle of unlocking  the door with the two
             knobs and the switch.
"""

even_Knob = int(input("What is the position of the first knob? (enter 1-12) "))
odd_Knob = int(input("What is the position of the second knob? (enter 1-12) "))
switch_Knob = input("What is the position of the switch? (enter up or down) ")

if switch_Knob == "up":
    switch_Knob = True
else:
    switch_Knob = False

if (even_Knob < 0 or even_Knob > 12) or (odd_Knob < 0 or odd_Knob > 12):
    print("Number set needs to be in between 1-12")
elif((even_Knob % 2 == 0) & (odd_Knob % 2 == 1)) & switch_Knob == True:
    print("the door opens and you get all the loot.")
elif ((even_Knob % 2 == 1) & (odd_Knob % 2 == 1)) & switch_Knob == True:
    print("The door clanks but doesn't open, Try again")
elif ((even_Knob % 2 == 0) or (odd_Knob % 2 == 1)) & switch_Knob == False:
    print("The door clanks but doesn't open, Try again")
else:
    print("the door doesn't budge")
