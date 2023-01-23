"""
File:         hw4_part3.py
Author:       Mohiuddin Syed
Date:         10/1/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Draws a circle from the users input radius
"""

if __name__ == "__main__":
    radius = int(input("What is the radius? (between 0 and 20) "))
    if radius < 0 or radius > 20:    # to check if its in boundraies
        print("Invalid radius")
    for y in range(-radius, radius + 1):    # -radius is the lowest value and the radius + 1 is the highest value (bot most left) (top most right)
        for x in range(-radius, radius + 1):
            if ((x**2) + (y ** 2)) <= radius ** 2:   # fills in the spaces condtion
                print('*', end='')
            else:
                print(' ', end='')
        print()          # Breaks the line
