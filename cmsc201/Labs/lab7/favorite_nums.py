"""
File:    favorite_nums.py
Author:  Mohiuddin Syed
Date:    10/23/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: ask the user to input a name and a favorite number. The system will tell whether or not the
             number already exists.


"""

def print_favorite_numbers(who, favorites):
    """
    :param who: this is a string, representing a person in our dictionary
    :param favorites: the favorite numbers dictionary
    :return: None
    """
    if who in favorites:
        print(favorites[who], end=":")
    elif who not in favorites:
        print("cannot print cause someone named {} exists".format(who))
    return


def add_favorite_number(who, number, favorites):
    """
    :param who: add "who" to the dictionary if they're not already there and give them a blank list
            otherwise, add the number to their favorites list if the number isn't already in someone's list.
    :param number: the number to add
    :param favorites: the favorites dictionary
    :return: None (dictionaries are mutable, so you don't need to return it to modify it)
    """

    Numb_checker = True
    for who in favorites:
        if number in favorites[who]:
            print('{} was found in {}\' favourites'.format(number, who))
            Numb_checker = False


    if Numb_checker == True:
        if who in favorites:
            print('{} was added to {}\'s favourites'.format(number, who))
            favorites[who].append(number)
        else:
            favorites[who] = [number]
        print('{} was added to {}\'s favourites'.format(number, who))


if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')
    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)
        if len(in_string.split()) == 2:
            who, num = in_string.split()
            num = int(num)
            add_favorite_number(who, num, favorites)

        in_string = input('What do you want to do (add favorite number), or quit? ')
