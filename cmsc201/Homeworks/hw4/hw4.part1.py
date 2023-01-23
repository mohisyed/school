"""
File:         hw4_part1.py
Author:       Mohiuddin Syed
Date:         10/1/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  play a game of rock paper scissors with the computer

"""
import sys
from random import choice, seed
if len(sys.argv) >= 2:
   seed(sys.argv[1])

if __name__ == "__main__":
    the_choice = choice(['rock', 'paper', 'scissors'])
    user_input = input("Enter rock, paper, or scissors to play, stop to end: ")

    print(the_choice)
    if user_input != "stop":     # if the user doesnt enter stop
        if user_input == the_choice:
            print("tie")

        elif user_input == "rock" and the_choice == "scissor":         # if user puts rock and the comp puts scissor
            print("{} beats {}".format(user_input, the_choice))

        elif user_input == "rock" and the_choice == "paper":
            print("{} loses to {}".format(user_input, the_choice))

        elif user_input == "scissors" and the_choice == "paper":
            print("{} beats to {}".format(user_input, the_choice))

        elif user_input == "scissors" and the_choice == "rock":
            print("{} loses to {}".format(user_input, the_choice))

        elif user_input == "paper" and the_choice == "rock":
            print("{} beats to {}".format(user_input, the_choice))

        elif user_input == "paper" and the_choice == "scissors":
            print("{} loses to {}".format(user_input, the_choice))
