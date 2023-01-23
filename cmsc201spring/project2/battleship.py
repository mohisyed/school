"""
File: battleship.py
File:    main.py
Author:  Mohiuddin Syed
Date:    5/1/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    This program is a battleship game.
"""
from board import *

# the constants for player board name
PLAYER_ONE_STRING = "player_one"
PLAYER_ONE_TARGET_STRING = "player_one_target"
PLAYER_TWO_STRING = "player_two"
PLAYER_TWO_TARGET_STRING = "player_two_target"
# the constants for hit and miss element of board
HIT_STRING = "X "
MISS_STRING = "O "
# the constants for result after shot
WIN_STRING = "win"
SUNK_STRING = "sunk"
AGAIN_STRING = "again"


class BattleshipGame:

    def run_game(self):
        """
        The main function to run game
        :param self
        """
        # ask player to place their ships
        print("Player 1, prepare to place your fleet.")
        # use display_boards function to show the board
        self.display_boards(PLAYER_ONE_STRING)
        # use place_ships function to place ship
        self.place_ships(self.board_one)

        print("Player 2, prepare to place your fleet.")
        # use display_boards function to show the board
        self.display_boards(PLAYER_TWO_STRING)
        # use place_ships function to place ship
        self.place_ships(self.board_two)

        # main while loop using finish as flag
        finish = False
        while not finish:

            # Player 1 shot action:
            # print player 1 info
            print("It's player 1 turn:")
            print("Player 1 board:")
            self.display_boards(PLAYER_ONE_STRING)
            print("Player 1 target board:")
            self.display_boards(PLAYER_ONE_TARGET_STRING)

            # player 1 while loop using end_turn flag for player 1 shot action
            end_turn = False
            while not end_turn:
                # ask player the target coordinates
                question = "Enter the coordinates to place the target: "
                # use ask_xy function to get x y input from player
                x, y = self.ask_xy(question)

                # use register_shot of board_two to get result from the shot
                result = self.board_two.register_shot(x, y)
                # get target board of player 1 to update
                player_board = self.board_one.get_board(False)

                # update target board and end_turn flag
                # if result is again, continue the player 1 loop
                if result == AGAIN_STRING:
                    end_turn = False
                # if hit or sunk ship, end the player 1 loop
                # and update target board
                if result == HIT_STRING or result == SUNK_STRING:
                    player_board[y][x] = HIT_STRING
                    end_turn = True
                # if miss, end the player 1 loop and update target board
                elif result == MISS_STRING:
                    player_board[y][x] = MISS_STRING
                    end_turn = True
                # if win, end the player 1 loop and update target board
                # then print winner, and set flag to end the main loop
                elif result == WIN_STRING:
                    player_board[y][x] = HIT_STRING
                    print("Player 1 Win!!!")
                    end_turn = True
                    # end the main loop
                    finish = True
            # end of the player 1 while loop

            # print the player 1 info after shot
            print("Player 1 result:")
            print("Player 1 board:")
            self.display_boards(PLAYER_ONE_STRING)
            print("Player 1 target board:")
            self.display_boards(PLAYER_ONE_TARGET_STRING)

            # if player 1 do not finish game, do the player 2 turn
            if not finish:
                # print player 2 info
                print("It's player 2 turn:")
                print("Player 2 board:")
                self.display_boards(PLAYER_TWO_STRING)
                print("Player 2 target board:")
                self.display_boards(PLAYER_TWO_TARGET_STRING)
                end_turn = False
                # player 2 while loop using end_turn flag
                # for player 2 shot action
                while not end_turn:
                    # ask player the target coordinates
                    question = "Enter the coordinates to place the target: "
                    # use ask_xy function to get x y input from player
                    x, y = self.ask_xy(question)

                    # use register_shot of board_one
                    # to get result from the shot
                    result = self.board_one.register_shot(x, y)
                    # get target board of player 2 to update
                    player_board = self.board_two.get_board(False)

                    # update target board and end_turn flag
                    # if result is again, continue the player 2 loop
                    if result == AGAIN_STRING:
                        end_turn = False
                    # if hit or sunk ship, end the player 2 loop
                    # and update target board
                    if result == HIT_STRING or result == SUNK_STRING:
                        player_board[y][x] = HIT_STRING
                        end_turn = True
                    # if miss, end the player 2 loop and update target board
                    elif result == MISS_STRING:
                        player_board[y][x] = MISS_STRING
                        end_turn = True
                    # if win, end the player 2 loop and update target board
                    # then print winner, and set flag to end the main loop
                    elif result == WIN_STRING:
                        player_board[y][x] = HIT_STRING
                        print("Player 2 Win!!!")
                        end_turn = True
                        finish = True
                # end of player 2 while loop

                # print the player 2 info after shot
                print("Player 2 result:")
                print("Player 2 board:")
                self.display_boards(PLAYER_TWO_STRING)
                print("Player 2 target board:")
                self.display_boards(PLAYER_TWO_TARGET_STRING)
            # end of the if for player 2 turn
        # end of the main while loop

    def __init__(self, size=10):
        """
        The constructor
        :param size: the size of the boards
        """
        # size of the board
        self.size = size
        # init the board for player 1
        self.board_one = Board(size)
        # init the board for player 2
        self.board_two = Board(size)

        # the dict of length of the ship
        self.length_dict = {
            "Ca": ["Carrier", 5],
            "Ba": ["Battleship", 4],
            "Cr": ["Cruiser", 3],
            "Su": ["Submarine", 3],
            "De": ["Destroyer", 2]
        }

    def display_boards(self, turn):
        """
        A function to print out the boards
        :param turn: the string to choose which board to print
        """
        # print player 1 board
        if turn == PLAYER_ONE_STRING:
            self.board_one.display_board(True)
        # print player 1 target board
        elif turn == PLAYER_ONE_TARGET_STRING:
            self.board_one.display_board(False)
        # print player 2 board
        elif turn == PLAYER_TWO_STRING:
            self.board_two.display_board(True)
        # print player 2 target board
        elif turn == PLAYER_TWO_TARGET_STRING:
            self.board_two.display_board(False)

    def place_ships(self, player_board):
        """
        A function to place ships to the player board
        :param player_board: the board to place ships
        """
        # go through all the ship in dict
        for ship in self.length_dict.keys():
            # get ship name
            ship_name = self.length_dict[ship][0]
            # get the length of the ship
            ship_length = self.length_dict[ship][1]

            # while loop to place ship
            done_place_ship = False
            while not done_place_ship:
                # ask user the x y coordinates
                question = "Enter x y coordinates to place the {}: " \
                    .format(ship_name)
                # get the start_pos by ask_xy function
                start_pos = self.ask_xy(question)

                # the get input while loop to get the direction of the ship
                done_get_input = False
                while not done_get_input:
                    go = input("Enter Right or Down (r or d) ")
                    # if the input is correct set flag to end get input loop
                    if go == "r" or go == "d":
                        done_get_input = True
                    else:
                        print("Invalid input, try again")

                # set the end_pos base on direction and start_pos
                if go == "r":
                    end_pos = [start_pos[0] + ship_length - 1, start_pos[1]]
                elif go == "d":
                    end_pos = [start_pos[0], start_pos[1] + ship_length - 1]

                # place the ship and set flag to end place ship while loop
                done_place_ship = player_board.place_ship \
                    (ship, start_pos, end_pos)

    def ask_xy(self, question):
        """
        A function to get the x y coordinates from user
        :param question: the string to print out question to ask user
        """
        # the while loop to get input
        done_get_input = False
        while not done_get_input:
            try:
                x, y = input(question).split()
                # check if x, y is digit
                if x.isdigit() and y.isdigit:
                    done_get_input = True
                else:
                    print("Invalid input, try again")
            except ValueError:
                print("Invalid input, try again")
        # get result as a list
        result = [int(x), int(y)]
        return result

if __name__ == '__main__':
    BattleshipGame().run_game()
