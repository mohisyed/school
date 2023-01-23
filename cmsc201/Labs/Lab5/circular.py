"""
File:         circular.py
Author:       Mohiuddin Syed
Date:         3/9/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  counts the rotation of user input 
"""

user_input = input("Enter a phrase: ")
for i in range(len(user_input)):
    print(i)
    print(user_input[i])

for k in range(len(user_input)):


user_input = user_input.lower()
user_input = user_input.strip()
user_input = user_input.split()
print("".join(user_input))
print(user_input)
