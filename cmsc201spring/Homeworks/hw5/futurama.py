"""
File:   futurama.py
Author:  Mohiuddin Syed
Date:    3/9/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Tells you what type of futurama characther you are
"""

user_input = input("Are you Human? ").lower()
if user_input == "yes":
    human_user_input = input("Is your family from mars? ").lower()
    if human_user_input == "yes":
        print("You are Amy Wong.")
    elif human_user_input == "no":
        mutant_user_input = input("Are you a mutant? ").lower()
        if mutant_user_input == "yes":
            print("You are Leela.")
        elif mutant_user_input == "no":
            activity_user_input = input("What is your favorite activity? (video games, filling, inventing)  ").lower()
            activity = ["video games", "inventing", "filling"]
            if activity_user_input in activity:
                if activity_user_input == "video games":
                    print("You are Phillip J Fry")
                elif activity_user_input == "inventing":
                    print("You are Hubert Farnsworth")
                elif activity_user_input == "filling":
                    print("You are Hermes Conrad")
            else:
                print("You are Scruffy The Janitor")
elif user_input == "no":
    nonhuman_user_input = input("Are you a robot? ").lower()
    if nonhuman_user_input == "yes":
        print("You are Bender")
    elif nonhuman_user_input == "no":
        print("You are Zoidberg")
