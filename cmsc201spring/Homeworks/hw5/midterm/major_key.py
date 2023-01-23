"""
File:    major_key.py
Author:  Mohiuddin Syed
Date:    3/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
finds the next steps in the diatonic scale

"""

the_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def get_scale(note):
    steps = [0, 2, 2, 1, 2, 2, 2]
    counter = 0
    if note in the_notes:
        for i in range(len(the_notes)):      # to find the index of the starting note
            if the_notes[i] == note:
                counter = i
        for i in range(7):
            counter = (counter + steps[i]) % 12          # keep it under 12 caues of the the notes is 12
            print(the_notes[counter], end=' ')
    else:
        print("Not a valid note")


if __name__ == '__main__':

    user_input = input("What major you want or enter Q to exit: ", ).upper()
    while user_input != "Q":
        get_scale(user_input)
        user_input = input("\nwhat major you want or enter Q to exit: ", ).upper()
