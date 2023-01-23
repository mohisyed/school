"""
File:    the_zoo.py
Author:  Mohiuddin Syed
Date:    4/13/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Creates a zoo and adds animals into the zoo


"""


class Animal:
    def __init__(self, name, species):
        self.name = name         # name of the animal
        self.species = species     # name of the species

    def display(self):
        print("The Animal named" + self.name + " is a " + self.species + ".")


class Zoo:
    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo  # name of zoo
        self.animals = {}  # create a dict

    def add_animal(self, the_animal):
        animal_name = the_animal.name
        self.animals[animal_name] = the_animal  # make a key

    def remove_animal(self, name):
        if name not in self.animals:    # name not in the dict
            print('{} is not one of the animals in the zoo.'.format(name))  # prints the animals not in zoo
        else:
            del self.animals[name]     # del the key

    def display(self):
        print("Here are the animals in " + self.name_of_zoo)
        for names in self.animals:    # scan the dict keys
            print("\t The animal named " + self.animals[names].name + " species "
                  + self.animals[names].species + ".")    # prints out the species


if __name__ == '__main__':
    national_zoo = Zoo('National Zoo')
    baltimore_zoo = Zoo('Baltimore Zoo')

    leo = Animal('Leo', 'Lion')
    gary = Animal('Gary', 'Giraffe')
    lauren = Animal('Lauren', 'Llama')
    emma = Animal('Emma', 'Emu')

    leo.display()
    gary.display()
    lauren.display()
    emma.display()

    national_zoo.add_animal(leo)
    national_zoo.add_animal(lauren)

    baltimore_zoo.add_animal(emma)
    baltimore_zoo.add_animal(gary)

    national_zoo.display()
    baltimore_zoo.display()

    national_zoo.remove_animal('Leo')
    baltimore_zoo.add_animal(leo)

    national_zoo.display()
    baltimore_zoo.display()

    national_zoo.remove_animal('Emma')

