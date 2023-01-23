"""
File:         worst_calculator.py
Author:       Mohiuddin Syed
Date:         9/10/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Calculates the sum of the integers and calulcates the product of the floats that you give it 
"""
whole_1 = int(input("Enter integer 1: "))
whole_2 = int(input("Enter integer 2: "))
sum = whole_1 + whole_2

float_1 = float(input("Enter Float 1: "))
float_2 = float(input("Enter Float 2: "))
float_3 = float(input("Enter Float 3: "))
product = float_1 * float_2 * float_3

print("the sum of the integers {} and {} is {}".format(whole_1,whole_2,sum))

print("the product of the floats {}, {} and {} is {}".format(float_1,float_2,float_3,product))
