"""
File:    recipe_maker.py
Author:  Mohiuddin Syed
Date:    5/14/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    recipe maker file
"""
import json

# CONSTANT
EXIT_SIGNAL = 'done'


def read_materials():
    name = input('Name the raw material? ')
    materials = {}
    while name != EXIT_SIGNAL:
        rate = int(input('What is the rate at which it is mined? '))
        # if material already in the lib, just ignore it
        if (name not in materials):
            materials.update({name: rate})
        name = input('Name the raw material? ')
    return (materials)


def read_one_recipe(output):
    rate_output = int(input('What is the rate at which it is output? '))

    ingredients = {}
    name = input('Name the ingredient: ')
    while not (name == 'stop' or name == 'done'):
        amount = int(input('How much of that ingredient is needed? '))
        # if material already in the lib, just ignore it
        if name not in ingredients:
            ingredients.update({name: amount})
        name = input('Name the ingredient: ')

    recipe = {"output": output, "output_count": rate_output, "part": ingredients}
    return (recipe)


def read_recipes():
    output = input('Name the output? ')
    recipes = {}
    while output != EXIT_SIGNAL:
        recipe = read_one_recipe(output)
        circo_check = False
        for key, value in recipe['part'].items():
            if have_circo(recipes, output, key):
                circo_check = True

        if output not in recipes and not circo_check:
            recipes.update({output: recipe})
        output = input('Name the output? ')
    return recipes


def have_circo(recipes, select_material, product_material):
    if product_material in recipes:
        for key, value in recipes[product_material]['part'].items():
            if select_material == key:
                return True
            elif have_circo(recipes, select_material, key):
                return True
    return False


if __name__ == '__main__':
    materials = read_materials()
    recipes = read_recipes()

    string_to_write = {"raw_materials": materials, "recipes": recipes}
    file_name = input('What is the file name? ')

    json_string = json.dumps(string_to_write)

    with open(file_name, 'wt') as jsfile:
        jsfile.write(json_string)

