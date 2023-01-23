"""
File:        hw1_part5.py
Author:      Mohiuddin Syed
Date:        9/11/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Calculates the Lorentz energy in object
"""
c = 299792458
restMass = float(input("What is the rest mass: "))
velocity = float(input("What is the velocity: "))

Lorentz_Einsten_equation = ((restMass)*(c**2))/((1-((velocity**2)/(c**2)))**(1/2))
print("The Lorentz Energy in the object with the rest mass {} and velocity {} is {}".format(restMass,velocity,Lorentz_Einsten_equation))
