"""
File:        hw2_part3.py
Author:      Mohiuddin Syed
Date:        9/17/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Guess the Star Trek Charachters through a bunch of nested if statments.
"""
print("Answer in yes or no.")
human = input("Is your character human? ")
if human == "yes":
    bald = input("Are they bald? ")
    if bald == "no":
        empath = input("Are they a Empath? ")
        if empath == "no":
            blind = input("Are they blind? ")
            if blind == "no":
                number_1 = input("Are they number 1? ")
                if number_1 == "yes":
                    print("You're thinking about Riker? ")
                else:
                    print("Shut up, Wesley. ")
            if blind == "yes":
                print("You're thinking about Geordi. ")
        if empath == "yes":
            print("You're thinking about Troi.")
    if bald == "yes":
        print("You're thinking about Captain Picard.")
if human == "no":
    kligon = input("Are they Klingon? ")
    if kligon == "no":
        android = input("Are they an android? ")
        if android == "no":
            print("Perhaps You're thinking about Mot The Barber??")
        if android == "yes":
            print("You're thinking about data")
    if kligon == "yes":
        print("You're thinking about Worf")
