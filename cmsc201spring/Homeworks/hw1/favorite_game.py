"""
File:    favorite_game.py
Author:  Mohi Syed
Date:    2/5/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Program asks user whats their favorite games and similar infomation
    and prints it out. Also calculates the hours played in a day

"""
fav_game = input('What is your favorite game to play? ')
number_of_players = input('How many players does the game have? ')
time_of_game = float(input("How many minutes have you played today? "))
hours_played = time_of_game / 60

print(
    "Your favorite game is " + fav_game + ", which has " + number_of_players + " players, and you have played", hours_played, "hours")
