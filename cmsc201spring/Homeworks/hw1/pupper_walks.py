"""
File:    pupper_walks.py
Author:  Mohi Syed
Date:    2/5/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Calulates how many miles the user has walked their dog in one year and also how many
    hours the user has walked their dog
"""
puppers = input("Whats pupper's name? ")
walks_per_week = float(input("How many times have you walked " + puppers + " this week? "))
how_many_miles = float(input("How long is the walk in miles? "))
length_miles_time = float(input("How many minutes does it take for you to walk a mile? "))

miles_per_year = how_many_miles * (walks_per_week * 52)
hours_per_year = (miles_per_year * length_miles_time) / 60

print("Your dog's name is", puppers, ", and you have walked", miles_per_year, "miles this year, in", hours_per_year,
      "hours.")
