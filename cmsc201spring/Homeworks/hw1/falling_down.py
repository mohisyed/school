"""
File:   falling_down.py
Author:  Mohi Syed
Date:    2/5/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Calculates the time it takes for a body to fall from a height above the surface of various interstellar bodies.

"""
planet = input("what planet are you on? ")
gravity_constant = float(input("What is the gravitational constant on " + planet + "? "))
height = float(input("What is the height of the object? "))

time = (((2 * height) / gravity_constant) ** (1/2))
print("The time it takes to fall from a height of", height, "to the surface of " + planet + " is", time, "seconds")

