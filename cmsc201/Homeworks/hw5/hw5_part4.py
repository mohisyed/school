"""
File:         hw5_part4.py
Author:       Mohiuddin Syed
Date:         10/14/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  a game in which creatures battle. The creatures have a a life, attack and first strike skill.
the last Creature standing wins


"""

def read_creature_file(creature_file_name):
    """
    :param creature_file_name: a json file with creature stats.
    :return: a python dictionary of creatures.
    """
    import json
    try:
        with open(creature_file_name) as f:
            return json.loads(f.read())
    except OSError:
        print('Unable to open the file, is it in the right place? ')

    return {}


def fight_creatures(first_creature, second_creature):
    """
    This should fight the two creatures.

    It should create and set an "alive" element in their dictionaries and if the creature is killed, set it to False.
    Each creature deals damage to the other, unless one has first strike, the other doesn't, and the creature with first strike deals fatal damage.
    Then the first strike creature does not receive damage.

    :param first_creature:
    :param second_creature:
    :return:
    """

    first_creature["alive"], second_creature["alive"] = False     # false so u can call it later in the second function
    first_creature_life_equ = 0     # the life's of the first equation not defined yet
    second_creature_life_equ = 0    # the life's of the second equation not defined yet

    if first_creature["first_strike"] and not second_creature["first_strike"]:       # first creature has first strike and the second creatures doesn't
        second_creature_life_equ = second_creature["life"] - first_creature["attack"]      # reassigin the variable
        if second_creature_life_equ > 0:                 # if there is still life in the second creature
            first_creature_life_equ = first_creature["life"] - second_creature["attack"]        # second creature attacks

    elif not first_creature["first_strike"] and second_creature["first_strike"]:    # second creature has first strike
        first_creature_life = first_creature["life"] - second_creature["attack"]
        if first_creature_life_equ > 0:
            second_creature_life_equ = second_creature["life"] - first_creature["attack"]
    else:                 # if they both dont have first strike or they both have it
        first_creature_life_equ = first_creature["life"] - second_creature["attack"]
        second_creature_life_equ = second_creature["life"] - first_creature["attack"]

    if first_creature_life_equ > 0:       # if health greater than 0 alive
        first_creature["alive"] = True

    if second_creature_life_equ > 0:
        second_creature["alive"] = True


if __name__ == '__main__':
    creatures = read_creature_file(input('What creature file do you want to load? '))
    if creatures:
        while input('Fight again?').strip().lower() in ['yes', 'y']:
            first_creature_name = input('What is the first creature? ')
            second_creature_name = input('What is the second creature? ')
            if first_creature_name in creatures and second_creature_name in creatures:
                first_creature = creatures[first_creature_name]
                second_creature = creatures[second_creature_name]
                fight_creatures(first_creature, second_creature)
                # hint, are these magic values? hmm... should you do this in your own code?
                print(first_creature_name, first_creature['attack'], first_creature['life'], first_creature['alive'])
                print(second_creature_name, second_creature['attack'], second_creature['life'],
                      second_creature['alive'])

                if first_creature['alive']:
                    print(first_creature_name, 'has survived the fight. ')
                else:
                    print(first_creature_name, 'has died in the fight. ')
                if second_creature['alive']:
                    print(second_creature_name, 'has survived the fight. ')
                else:
                    print(second_creature_name, 'has died in the fight. ')
            else:
                print('One of the creatures wasn\'t in the list of creatures')


