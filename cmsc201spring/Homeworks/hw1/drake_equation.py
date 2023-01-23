"""
File:   drake_equation.py
Author:  Mohi Syed
Date:    2/5/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Program that uses the drake equation to predict
    how many trasmitting sentient spieces exist. Program
    askes user for the info
"""
rate_star_formation = float(input("What is the average rate of star formation in our galaxy per year? "))
fraction_of_star_planets = float(input("What is the fraction of the stars with planets? "))
planets_per_habitable = float(input("What is the average number of planets per system that are habitable? "))
actually_planet_support_life = float(input("How many habitable planets actually support life? "))
intellegient_planet_life = float(input("How many planets with life have intelligent life? "))
transmit_deep_space = int(input("How long in years does the average civilization transmit into deep space? "))

tranmitting_equation = rate_star_formation * fraction_of_star_planets * planets_per_habitable * actually_planet_support_life * intellegient_planet_life * transmit_deep_space

print("There are on average {} transmitting civilizations at any time in our galaxy.".format(tranmitting_equation))
