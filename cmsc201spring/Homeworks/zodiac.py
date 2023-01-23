"""
File:    zodiac.py
Author:  Mohiuddin Syed
Date:    2/14/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    user inputs a year and the program will tell you the zodiac
    animal for that year.

"""
year = int(input("What is the year that you want to convert? "))

divide = (year - 5) % 12

if divide == 0:
        print("This is the year of the ox")
elif divide == 1:
        print("This is the year of the tiger")
elif divide == 2:
        print("This is the year of the rabbit")
elif divide == 3:
        print("This is the year of the dragon")
elif divide == 4:
        print("This is the year of the snake")
elif divide == 5:
        print("This is the year of the horse")
elif divide == 6:
        print("This is the year of the goat")
elif divide == 7:
        print("This is the year of the monkey")
elif divide == 8:
        print("This is the year of the rooster")
elif divide == 9:
        print("This is the year of the dog")
elif divide == 10:
        print("This is the year of the pig")
elif divide == 11:
        print("This is the year of the rat")
        
