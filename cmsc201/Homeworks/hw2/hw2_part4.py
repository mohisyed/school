"""
File:        hw2_part4.py
Author:      Mohiuddin Syed
Date:        9/16/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Tells the user if the year they inputted was a leap year or not.
"""
user_Year = int(input("Which year do you want to know if it is a leap year? "))
if user_Year % 4 ==0:
    if user_Year % 100 == 0:
        if user_Year % 400 == 0:
            print("A leap year")
        else:
            print("Not a leap year")
    else:
        print("A leap year")
else:
    print("not a leap year")
