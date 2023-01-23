"""
File:   monster_battle.py
Author:  Mohiuddin Syed
Date: 2/14/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    User inputs power level of two monsters. The monster with the higher
    power level wins and displays back to the user that the monster won.

"""

monster_1_name = input("What is the first monster name? ")
monster_1_power = int(input("What is the power level of the first monster? "))

monster_2_name = input("What is the second monster name? ")
monster_2_power = int(input("What is the power level of the second monster? "))

if monster_1_power > monster_2_power:
        print("{} wins!".format(monster_1_name))
elif monster_1_power < monster_2_power:
        print("{} wins!".format(monster_2_name))
else:
        print("Draw!")
        
