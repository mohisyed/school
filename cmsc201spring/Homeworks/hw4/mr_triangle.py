"""
File:    mr_triangle.py
Author:  Mohiuddin Syed
Date:    2/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
Program takes user input and creates a triangle from the parameters the user inputs.


"""

user_height = int(input("How high is the triangle going to be? "))
Symbol_input = input("What symbol do you want to use? ")


if user_height < 0:
    print("Need a positive number.")
elif user_height > 0:
    if len(Symbol_input) == 1:
        for i in range(user_height + 1):
            print(Symbol_input * i)
    else:
        print("Must use one character only") 
