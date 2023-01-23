"""
File:    fizz_buzz.py
Author:  Mohiuddin Syed
Date:    2/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
program takes user input and tells the user whether or not the input
is divisible by 4 ,9 or both


"""

user_input = int(input("what is the top number do you want to check? "))
for i in range(user_input + 1):
    if i % 4 == 0 and i % 9 == 0:
        print("{}: This is a very special time".format(i))
    elif i % 4 == 0:
        print("{} : Four?  What is it good for? Absolutely nothing!".format(i))
    elif i % 9 == 0:
        print("{}: A stitch in time saves nine.".format(i))
