"""
File:    Pyopoly.py
Author:  Mohiuddin Syed
Date:    10/21/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: Play the game of pyopoly.

"""

from sys import argv

from random import randint, seed
from board_methods import load_map, display_board

if len(argv) >= 2:
    seed(argv[1])
QUIT_STRING = 'quit'


def play_game(starting_money, pass_go_money, board_file):      # main function holds all the other function
    dice_1 = randint(1, 6)    # dice constant
    dice_2 = randint(1, 6)
    pass_go_money_dict = pass_go_money      # originally the dict just a variable for the pass go money

    player1_dict["money"] = starting_money
    player1_role = dice_1 + dice_2           # player 1 role
    player2_role = dice_1 + dice_2
    if user_turn == True:                     # flips user turns
        while player1_dict["money"] != 0:       # money not equal to 0
            player1_role = dice_1 + dice_2
            format_display(player1_role, player2_role, board_file)
            print(player1_role)
            player_turn(board_file)            # calls the player_turn
            if player1_dict["position"] == 0 or player2_dict["position"] == 0:    # player position == 0
                player1_dict["money"] += pass_go_money_dict
                player2_dict["money"] += pass_go_money_dict
            user_turn == False
            if player1_dict["money"] == 0:
                print("GAME OVER")
                game_state = False
    else:           # Player 2 turn
        while player2_dict["money"] != 0:
            print("user 2")
            player2_role = dice_1 + dice_2
            format_display(player1_role, player2_role, board_file)
            print(player2_role)
            player_turn(board_file)
            if player1_dict["position"] == 0 or player2_dict["position"] == 0:
                player1_dict["money"] += pass_go_money_dict
                player2_dict["money"] += pass_go_money_dict
            if player2_dict["money"] == 0:
                print("GAME OVER")
                game_state = False
            user_turn == True


def player_turn(board):
    print("(1) Buy Property \n(2) Get Property Info\n(3) Get Player info\n(4) End turn")
    user_menu = int(input("What do u want to do? "))

    if user_menu != 4:      # if user input enters a value
        if user_menu == 1:
            buy_property(board)
        if user_menu == 2:
            prop_info(board)
        if user_menu == 3:
            player_info(board)
    else:
        user_turn == False      # switches to user 2


def buy_property(board):
    tracker_position = -1   # tracker position
    tracker_price = 0       # his price
    name = ""

    for line in load_map(board):
        tracker_position += 1
        if tracker_position == player1_dict["position"]:     # if his position is equal to the tracker
            if player1_dict["ownership"] or player2_dict["ownership"] in line["Place"]:
                if player1_dict["ownership"] in line["Place"]:
                    print("sorry cant buy this its owned by {}".format(player1_dict["name"]))
                elif player2_dict["ownership"] in line["Place"]:
                    print("sorry cant buy this its owned by {}".format(player2_dict["name"]))
            else:
                # check to see if its owned (IF)
                # if un owned then say input("The property is unowned, do you want to buy it?" ) accept yes or no only
                tracker_price = int((line["Price"]))
                name = line["Place"]

    if tracker_price > 0:     # if the price is greater than 0  (to check -1)
        if player1_dict["money"] >= tracker_price:
            player1_dict["money"] -= tracker_price
        else:
            print(player1_dict)
            # del player1_dict["ownership"]
    print("you have bought {} ".format(name))


def prop_info(board):
    check_input = input("which property? (abbrev) ")
    for line in load_map(board):    # load map
        if check_input == line["Abbrev"]:    # check if input is the smae as any of the abbrevs
            print(line["Place"])
            print("Price: ", line["Price"])
            if player1_dict["ownership"] or player2_dict["ownership"] == check_input:
                if player1_dict["ownership"] == check_input:
                    print(player1_dict["name"])
                elif player2_dict["ownership"] == check_input:
                    print(player2_dict["name"])
            print(line["Rent"])
            # put another if statement checking ownership


def player_info(board):
    x = input("Which player do u want to know about? ")
    if player1_dict["name"] == x:
        print("name: ", player1_dict["name"])
        print("Symbol: ", player1_dict["symbol"])
        print("Current money :", player1_dict["money"])
        print("Properties owned: ", player1_dict["ownership"])
    elif player2_dict == x:
        print("name: ", player2_dict["name"])
        print("Symbol: ", player2_dict["symbol"])
        print("Current money :", player2_dict["money"])
        print("Properties owned: ", player2_dict["ownership"])


def format_display(player, player2, board):
    the_board = []
    the_real_board = []
    for line in load_map(board):
        the_board.append((line["Abbrev"]))
    for i in range(len(the_board)):
        the_real_board.append(
            the_board[i].format(i)[0:5].ljust(5) + '\n     ')

    if user_turn:
        position = player1_dict["position"]
        move = player
        if player >= 0:
            position += int(move)
            position %= len(the_real_board)
            copy_board = list(the_real_board)
            copy_board[position] = copy_board[position][0:6] + player1_dict["symbol"]
            display_board(copy_board)
        player1_dict["position"] = position
    elif not user_turn:
        position = player2_dict["position"]
        move = player2
        if player >= 0:
            position += int(move)
            position %= len(the_real_board)
            copy_board = list(the_real_board)
            copy_board[position] = copy_board[position][0:6] + player2_dict["symbol"]
            display_board(copy_board)
        player2_dict["position"] = position


if __name__ == '__main__':
    player1_dict = {"name": input("what is your name player 1? "), "money": 0, "position": 0, "ownership": []}
    player1_dict["symbol"] = input("What is your symbol {}? ".format(player1_dict["name"]))
    player2_dict = {"name": input("what is your name player 2? "), "money": 0, "position": 0, "ownership": []}
    player2_dict["symbol"] = input("What is your symbol {}? ".format(player2_dict["name"]))
    print(player1_dict, player2_dict)

    user_turn = True
    game_state = True
    while game_state:
        play_game(1500, 200, "proj1_board1.csv")
