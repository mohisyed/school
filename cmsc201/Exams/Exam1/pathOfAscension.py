"""
File:         pathOfAscension.py
Author:       Mohiuddin Syed
Date:         10//2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  prints a random list and tells the user the longest ascending subequence is.

"""
import sys
from random import seed, randint

# make sure you include this for testing purposes:
if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":
    ascension_list = []
    second_list = []
    count = 0
    fake_count = 0
    user_input = int(input("What length of sequence do you want to input? "))

    for i in range(user_input):
        ascension_list.append(randint(0, 100))

    for i in range(len(ascension_list) - 1):
        if ascension_list[i] > ascension_list[i + 1]:    # first ascension list greater than second ascension list
            fake_count += 1           # fake count
        else:
            if fake_count > count:    # fake count is greater than count
                count = fake_count
            fake_count = 1
    if fake_count > count:
        fake_count = count

    print(ascension_list)
    print("The max ascending length ", count)

