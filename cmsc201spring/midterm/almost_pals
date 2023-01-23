"""
File:    almost_pals.py
Author:  Mohiuddin Syed
Date:    4/24/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    check for palindromes
"""


def check_palindromes(word, counter):  # takes the word and the counter (distance)
    if len(word) < 2:
        return counter

    if word[0] != word[-1]:
        counter += 1
    return check_palindromes(word[1:-1], counter)


word = input("Enter a word to test: ")  # input to test
print(check_palindromes(word, 0))
