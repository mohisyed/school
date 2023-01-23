"""
File:         hw3_part2.py
Author:       Mohiuddin Syed
Date:         9/26/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Calculates the Faulhaber Sum
"""
if __name__ == "__main__":
    numberofterms = int(input("What is number of terms? "))
    powerofterms = int(input("What is power of the terms? "))

    sum = 0
    x = []

    if numberofterms < 0 or powerofterms < 0:      #one or both variables cannot be negative
        print("Terms cannot be negative")

    for i in range(numberofterms):            #creates the 1,2,3 ... sequence
        x.append(i+1)

    for i in range(len(x)):
        faulhaber_squaring = (x[i]**powerofterms)       #squares the sequances
        sum = sum + faulhaber_squaring                  #adds the sequances together

    print(sum)
