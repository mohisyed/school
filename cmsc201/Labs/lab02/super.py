"""
File:         super.py
Author:       Mohiuddin Syed
Date:         2/17/2018
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Ask user if or not they are a villian or hero. If selcted hero
              they are asked how many civilians they saved. If villian is selected
              asked for an name then displays a message.
"""
              
user_input = (input("Are you a hero or a villian? "))
if user_input == "hero":
    people_saved = int(input("How many people have u saved? "))
    if people_saved <= 10:
        print("Go on more patrols! ")
    if 10 < people_saved < 100:
        print("Sounds like your making a difference! ")
    if people_saved >= 100:
        print("Wow, great job saving the city ")

if user_input == "villian":
    name = input("What is your name? ")
    print("{} sounds pretty evil to me!".format(name))
