"""
File:        hw2_part5.py
Author:      Mohiuddin Syed
Date:        9/16/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Ask the user for an angle. Depending on the angle they input the system will
            tell them what path of enlightment there angle lands on
"""

user_input = int(input("enter an angle to determine the point on the Eightfold Path: "))
x = int(user_input % 360)
if user_input % 45 == 0:
    if x == 0:
        print("You have selected {} degrees and the Right Resolve path".format(user_input))
    if x == 45:
        print("You have selected {} degrees and the Right View path".format(user_input))
    if x == 90:
        print("You have selected {} degrees and the Right Samadhi".format(user_input))
    if x == 135:
        print("You have selected {} degrees and the Right Mindfulness path".format(user_input))
    if x == 180:
        print("You have selected {} degrees and the Right Effort path path".format(user_input))
    if x == 225:
        print("You have selected {} degrees and the Right Livelihood".format(user_input))
    if x == 270:
        print("You have selected {} degrees and the Right Conduct path ".format(user_input))
    if x == 315:
        print("You have selected {} degrees and the Right Speech path".format(user_input))
else:
    print("You have not reached enlightenment yet, try an angle divisible by 45")
