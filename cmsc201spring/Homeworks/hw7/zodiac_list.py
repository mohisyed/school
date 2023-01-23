"""
File:    zodiac_list.py
Author:  Mohiuddin Syed
Date:    2/24/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    user inputs a year and the program will tell you the zodiac
    animal for that year.

"""
year = int(input("What is the year that you want to convert? "))
divide = (year - 5) % 12
zodiac = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]

if divide == 0:
    print("This is the year of the {}".format(zodiac[0]))
elif divide == 1:
    print("This is the year of the {}".format(zodiac[1]))
elif divide == 2:
    print("This is the year of the {}".format(zodiac[2]))
elif divide == 3:
    print("This is the year of the {}".format(zodiac[3]))
elif divide == 4:
    print("This is the year of the {}".format(zodiac[4]))
elif divide == 5:
    print("This is the year of the {}".format(zodiac[5]))
elif divide == 6:
    print("This is the year of the {}".format(zodiac[6]))
elif divide == 7:
    print("This is the year of the {}".format(zodiac[7]))
elif divide == 8:
    print("This is the year of the {}".format(zodiac[8]))
elif divide == 9:
    print("This is the year of the {}".format(zodiac[9]))
elif divide == 10:
    print("This is the year of the {}".format(zodiac[10]))
elif divide == 11:
    print("This is the year of the {}".format(zodiac[11]))
