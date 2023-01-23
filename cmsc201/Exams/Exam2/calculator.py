"""
File:    calculator.py
Author:  Mohiuddin Syed
Date:    11/22/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: calcualtor
"""

def create(list):





if __name__ == "__main__":
    fileinput = input("what type of file do you want to run: ")
    open(fileinput, "r")
    lines = fileinput.readlines()
    for line in lines:
        inputx = line.lower().split(" ")

