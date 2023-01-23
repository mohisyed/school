"""
maybe
import csv
"""
import json

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'


def connect_switchboards(switchboards, area_1, area_2):
    if area_2 not in switchboards[area_1][1] or area_1 not in switchboards[area_2][1]:
        switchboards[area_1][1].append(area_2)
        switchboards[area_2][1].append(area_1)
        print(switchboards)
    else:
        print("Connection already exits ")

def add_switchboard(switchboards, area_code):
    checker = switchboards.keys()
    if area_code not in checker:
        switchboards[area_code] = [[], [], []]           # phone number, connections and phone connections
        print(switchboards)
        print("true")
    else:
        print("already exists")
    return switchboards


def add_phone(switchboards, area_code, phone_number):
    checker = switchboards.keys()
    if area_code in checker:
            switchboards[area_code][0].append(phone_number)
            print(switchboards)
    else:
        print("switchboard doesen't exist")


def save_network(switchboards, file_name):
    with open("file_name.json", "w") as outfile:
        json.dump(switchboards, outfile)

def load_network(file_name):
    """
    :param file_name: the name of the file to load.
    :return: you must return the new switchboard network.  If you don't, then it won't load properly.
    """
    with open("file_name.json") as json_file:
        return json.load(json_file)


def start_call(switchboards, start_area, start_number, end_area, end_number):
    counter = 0
    # iterate through the switchboard key check to see if area code not
    # start area = end area
    keys = []
    for key in switchboards.keys():
        keys.append(key)

    for i in range(switchboards.keys()):
        recursion_call = start_call(switchboards, keys[i], start_number, end_area, end_number)
        if i not in keys:
            return True
        else:
            if recursion_call:
                return True
    return False


    # go through list of phones
        # check to see if the phone numbers are correct
        # return phone
       # else
   


"""
    if switchboards[start_area][1] == end_area:
        if switchboards[start_area][2] != end_number:
            switchboards[start_area][2].append(end_number)
            switchboards[end_area][2].append(start_number)
            print("Connection has been established")
            return switchboards[start_area][2]
        else:
            print("number already here ")
            return switchboards[start_area][2]
    else:
        print("connection has not been established")
        return switchboards[start_area][2]
"""

        




def end_call(switchboards, start_area, start_number):
    pass


def display(switchboards):
    key_names = []
    for key in switchboards.keys():
        key_names.append(key)
    for i in switchboards.keys():
        x = key_names[i]
        print("Switchboard with area code: ", key_names[i])
        print("Trunk lines are:")
        print("Trunk line connection to:", switchboards[x][1])
        print("local phone numbers are: ")
        if switchboards[x][2] is not None:
            for i in len(switchboards[x][2]):
                print("phone with number is: ", switchboards[x][2][i])






if __name__ == '__main__':
    switchboards = {}
    # switchboards = [[], []]  # probably {} or []           come back to if dict dosent work
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            connect_switchboards(switchboards, area_1, area_2)
        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            add_switchboard(switchboards, int(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))
            add_phone(switchboards, area_code, phone_number)
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            save_network(switchboards, split_command[1])
            print('Network saved to {}.'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            switchboards = load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))
        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))
            start_call(switchboards, src_area_code, src_number, dest_area_code, dest_number)

        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))
            end_call(switchboards, area_code, number)

        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            display(switchboards)

        s = input('Enter command: ')


