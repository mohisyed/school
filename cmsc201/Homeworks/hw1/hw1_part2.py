"""
File:        hw1_part2.py
Author:      Mohiuddin Syed
Date:        9/11/2020
Section:     24
E-mail:      msyed2@umbc.edu
Description: Ask the user what's their favorite pokemon, the type and a move of the pokemon.
            Then tells the user what their favorite pokemon is, their type and move

"""
pokemonName = input("What is your favorite pokemon: ")
pokemonType = input("What type is {}: ".format(pokemonName))
pokemonMove= input("What move does {} have: ".format(pokemonName))

print("{} is a {} type and has {} as a move".format(pokemonName,pokemonType,pokemonMove))
