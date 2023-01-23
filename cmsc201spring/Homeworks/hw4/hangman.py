"""
File:    hangman.py
Author:  Mohiuddin Syed
Date:    2/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
user plays a hangman game
"""

user_input = input("What is the word or choose 'quit' to exit: ").lower()
hangman_underscores = "_" * len(user_input)
hangman_underscores = list(hangman_underscores)

if user_input == 'quit':
    print("thank you for playing")
elif user_input != 'quit':
    while "_" in hangman_underscores:
        second_user = input("Enter a letter to guess for the word (MUST BE ONE LETTER): ").lower()
        if len(second_user) != 1:
            print("Has to be one letter")
        else:
            if second_user in user_input:
                for i in range(len(user_input)):
                    if user_input[i] == second_user:
                        hangman_underscores[i] = second_user
                print(hangman_underscores)
            elif second_user not in user_input:
                print("{} is not in the word".format(second_user))
                print(hangman_underscores)
    print("Congrats you have finished")
