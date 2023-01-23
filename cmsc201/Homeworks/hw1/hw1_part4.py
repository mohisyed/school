"""
File:        hw1_part4.py
Author:      Mohiuddin Syed
Date:        9/11/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: tells the salesman commission from the gross profit
"""
car_price = int(input("Enter the cars price: "))
gross_profit = car_price * .05
salesman_profit = gross_profit* .25

print("You made {} dollars commission on that car sale.".format(salesman_profit))
