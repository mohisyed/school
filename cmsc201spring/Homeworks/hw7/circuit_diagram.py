"""
File:    circuit_diagram.py
Author:  Mohiuddin Syed
Date:    2/14/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    User inputs numbers between 1 and 0. Program takes the number
    and sees if the circuit board can work
"""

a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))
d = int(input("Enter d "))
e = int(input("Enter e "))

b_and_c = b and c
not_d = not d
b_and_c_not_d = b_and_c or not_d or e

if a == b_and_c_not_d:
        print("The circuit outputs ", a)
else:
        print("The circuit outputs ", 0)
        
