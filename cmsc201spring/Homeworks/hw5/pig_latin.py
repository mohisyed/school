
"""
File:   pig_latin.py
Author:  Mohiuddin Syed
Date:    3/9/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    converts the the input to pig latin
"""
user_input = input("Enter a sentence to convert: ").lower()
#user_input = user_input.split()

Vowels = ['a', 'e', 'i', 'o', 'u']
consants = []
index_vowel = 0
pigtext = ""

x = -1
while index_vowel == 0:     # find length of the first vowel
    x += 1
    if user_input[x] in Vowels:
        index_vowel = x

for i in range(index_vowel):      # convert to ay
    pigtext += user_input[i]

pigtext += "ay"           # adds ay

if user_input[:index_vowel] == "":
    user_input = user_input + pigtext
else:
    user_input = user_input[index_vowel:] + pigtext

print(user_input)
