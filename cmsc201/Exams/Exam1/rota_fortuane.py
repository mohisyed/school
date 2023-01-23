"""
File:         Rota_Fortunae.py
Author:       Mohiuddin Syed
Date:         10/7/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Hang man like game. enter a phrase and guess. as you correctly answer _ will fill up
"""
solve_list = []
guess_list = []
inital_solve_input = input("What is the word you want the players to guess? ")
solve_list = list(inital_solve_input)

for i in range(len(solve_list)):   # makes the ___ the list
    if solve_list == " ":
        guess_list.append(i)       # adds the i to list
    else:
        guess_list.append("_")     # creates the __

while "_" in guess_list:
    for i in guess_list:
        print(i, " ")    # sub the i to a space
    print()

second_solve_input = input("Guess a letter, or 'solve' ")

if second_solve_input == "solve":
    second_solve_input = input("Guess a letter, or 'solve' ")
    if second_solve_input == solve_list:
        print("You win")
        second_solve_input = "solve"
    else:
        print("Wrong guess")
else:
    if len(second_solve_input) == 1:    # if one letter
        if second_solve_input not in solve_list:   # not in list
            if second_solve_input.upper() not in solve_list and second_solve_input.lower() not in solve_list:    # one last cond saying if upper and lower case version is not in list
                guess_list.append(second_solve_input)
                print('There are no', second_solve_input, "'s in the phrase")
        else:         # if in list
            solve_list.append(second_solve_input)
            for i in range(len(solve_list)):
                if solve_list[i] == second_solve_input.lower():   # convert the _ to a letter
                    guess_list[i] = solve_list[i]
                elif solve_list[i] == second_solve_input.upper():
                    guess_list[i] = solve_list[i]
            else:
                print("you have already guessed the letter")
    else:
        print("Enter a single char")

print("u win")
