"""
File:        hw1_part3.py
Author:      Mohiuddin Syed
Date:        9/11/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Calculates the total cost of owning a animal
"""

pet_type = input("What type of animal do you own? ")
monthly_food = int(input("How much money do you spend on food per month for your {} ? ".format(pet_type)))
monthly_supplies = int(input("How much money do spend on {} supplies? ".format(pet_type)))

annual_cost = (monthly_food + monthly_supplies) * 12

print("The annual cost of owning an {} is {}".format(pet_type,annual_cost))
