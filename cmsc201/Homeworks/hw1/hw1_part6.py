"""
File:        hw1_part6.py
Author:      Mohiuddin Syed
Date:        9/11/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Calculates the distance between two gravitational bodies 
"""
G_constant = 6.674*(10**-11)
mass_obj1 = float(input("What is the mass for the first object in kg: "))
mass_obj2 = float(input("What is the mass for the second object in kg: "))
distance = float(input("What is the distance between the objects in meters: "))

formula = (G_constant * mass_obj1 * mass_obj2)/ (distance**2)
print("The gravitational force between the two objects is :", formula)
