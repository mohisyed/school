"""
File:         Diphtongs.py
Author:       Mohiuddin Syed
Date:         10/7/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Program prints the diphtongs and tells the user how many diphthongs are in the user phrase
"""

vowels = ["a", "e", "i", "o", "u", "y"]
second_vowels = []
counter = 0
user_input = input("Enter a string with a lot of diphthongs: ")
user_input.lower()

for i in range(len(user_input)-1):
    if user_input[i] in vowels and user_input[i+1] in vowels:      # user input in vowels and the second userinput is in vowels
        if user_input[i] not in second_vowels and user_input[i+1] not in second_vowels:     # user input not in second list and second user input not in second list
            print(user_input[i] + user_input[i+1])
            second_vowels.append(user_input[i])
            second_vowels.append(user_input[i+1])
            counter += 1

print("The diphthong counter is ", counter)





