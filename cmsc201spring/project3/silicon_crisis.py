"""
File:    silicon_crisis.py
Author:  Mohiuddin Syed
Date:    4/24/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    slilcion file
"""
import json


class mine:
    # None == inactive
    def __init__(self):
        self.material = None
        self.rate = 0

    ''' 
    Function to set the mine to specified material.
    Paraments:
        raw_meterials: Dictionary contains all the raw materials and its rate
        select_material: String - the user input
    Tasks:
        If the mine already set a specified material, return false
        If select_material exists in raw_materials, change mine status to active and return false
        else return false
    Returns:
        True: Successful.
        False: Unsuccessful
    '''

    def set_material(self, raw_materials, select_material):
        if self.material != None:
            return False
        if select_material in raw_materials:
            self.material = select_material
            self.rate = raw_materials[select_material]
            return True
        return False

    ''' 
    Function to display its infomation itself
    '''

    def display(self):
        if (self.material):
            print('\t\t' + self.material + ' mine producing ' + str(self.rate) + ' per turn')
        else:
            print('\t\tMine Currently Inactive')

    ''' 
    Function to get the mine work in the turn

    Paraments:
        StockPile: Current StockPile

    Returns:
        List:
            List[0]: Name of material.
            List[1]: Rate
    '''

    def work(self, StockPile):
        if not self.material:
            return None
        return [self.material, self.rate]


class factory:
    def __init__(self):
        self.material = None
        self.rate = 0
        self.total = 0
        self.parts = {}

    def set_material(self, recipes, select_recipe):
        if self.material != None:
            return False
        if select_recipe in recipes:
            value = recipes[select_recipe]
            self.material = value['output']
            self.rate = value['output_count']
            self.parts = value['part']
            return True

        return False

    def display(self):
        if self.material:
            print(
                '\t\t' + self.material + ' factory producing ' + str(self.rate) + ' per turn, total production ' + str(
                    self.total))
        else:
            print('\t\tFactory Currently Inactive')

    '''
    Like mine class, but return type of material, rate and all the parts of its
    '''

    def work(self, StockPile):
        if not self.material:
            return None
        for key, value in self.parts.items():
            if (StockPile.materials[key] < value):
                return None
        self.total += self.rate
        return [self.material, self.rate, self.parts]


class stockpile:

    def __init__(self, raw_materials, recipes):
        self.materials = {}
        self.recipes = {}
        for key, value in raw_materials.items():
            self.materials.update({key: 0})
        for key, value in recipes.items():
            self.materials.update({key: 0})
        self.recipes = recipes

    def display_materials(self):
        print(':::Current Stockpile:::')
        for key, value in self.materials.items():
            if value > 0:
                print('\t' + key + ': ' + str(value))

    def display_recipe(self):
        print(':::Recipes:::')
        for key, value in recipes.items():
            print('\t' + key + ' - produced in increments of ' + str(value['output_count']))
            print('\tRequired Materials:')
            for part, number in value['part'].items():
                print('\t  ' + part + ': ' + str(number))

    def work_mine(self, mine_result):
        if mine_result != None:
            self.materials[mine_result[0]] += mine_result[1]

    def work_factory(self, factory_result):
        if factory_result != None:
            for key, value in factory_result[2].items():
                self.materials[key] -= value
            self.materials[factory_result[0]] += factory_result[1]


def query(recipes, select_material, product_material):
    count = 0
    if product_material in recipes:
        for key, value in recipes[product_material]['part'].items():
            if select_material == key:
                count += value
            else:
                count += value * query(recipes, select_material, key)
    return count


if __name__ == '__main__':
    file_name = input('Enter SC Recipe File Name: ')
    with open(file_name, 'r') as jsonfile:
        json_string = jsonfile.read()
    dictionary_json = json.loads(json_string)

    raw_materials = dictionary_json['raw_materials']
    recipes = dictionary_json['recipes']

    Mine = []  # list mine
    Factory = []  # list factory
    StockPile = stockpile(raw_materials, recipes)

    Mine.append(mine())
    Mine.append(mine())
    Factory.append(factory())
    Factory.append(factory())

    quit = False
    turn_count = 1
    while not quit:
        action = input('Select Next Action>> ').split()
        if action[0] == 'set':
            if action[1] == 'mine':
                Mine[int(action[2])].set_material(raw_materials, action[3])
            if action[1] == 'factory':
                Factory[int(action[2])].set_material(recipes, action[3])
        if action[0] == 'display':
            if action[1] == 'mines':
                i = 0
                for _mine in Mine:
                    print('\tMine ' + str(i))
                    _mine.display()
                    i = i + 1

            if action[1] == 'factories':
                i = 0
                for _factory in Factory:
                    print('\tFactory ' + str(i))
                    _factory.display()
                    i = i + 1

            if action[1] == 'stockpile':
                StockPile.display_materials()

            if action[1] == 'recipes':
                StockPile.display_recipe()

        if action[0] == 'end':
            if action[1] == 'turn':
                print('Making...')
                for _mine in Mine:
                    StockPile.work_mine(_mine.work(StockPile))
                print('Making...')
                for _factory in Factory:
                    StockPile.work_factory(_factory.work(StockPile))

                if (StockPile.materials['factory'] > 0):
                    for i in range(StockPile.materials['factory']):
                        Factory.append(factory())
                    StockPile.materials['factory'] = 0

                if (StockPile.materials['mine'] > 0):
                    for i in range(StockPile.materials['factory']):
                        Mine.append(mine())
                    StockPile.materials['mine'] = 0
                print('Turn ' + str(turn_count) + ' Complete')
                turn_count += 1
        if action[0] == 'how':
            print(query(recipes, action[2], action[6]))
        if action[0] == 'quit':
            quit = True
