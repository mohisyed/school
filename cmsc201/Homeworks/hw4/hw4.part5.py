"""
File:         hw4_part1.py
Author:       Mohiuddin Syed
Date:         10/1/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Play a guessing game with the computuer
"""
import sys
from random import randint, seed
if len(sys.argv) >= 2:
   seed(sys.argv[1])

if __name__ == "__main__":

    comp_guess = randint(1, 100)    # computer guess from between 1-100
    guess_input_tracker = 1         # user guess tracker (starts at 1 because first guess dosent get accounted)
    guess_input_answer = 0          # empty input variable

    while guess_input_answer != comp_guess:
        guess_input_answer = int(input("Guess a number between 1 and 100: "))
        if guess_input_answer < comp_guess:      # if user guess less than comp guess
            print("Your guess is to low")
            guess_input_tracker += 1
        elif guess_input_answer > comp_guess:   # if user guess greater than comp guess
            print("Your guess is to high")
            guess_input_tracker += 1 

    if guess_input_answer == comp_guess:       # if user guess equals comp guess
        print("You have guessed the correct answer. You took {} tries".format(guess_input_tracker))
