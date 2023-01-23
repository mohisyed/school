from sys import argv
from random import choice
from board_square_starter import BoardSquare, UrPiece
"""
File:    royal_game_of_ur.py
Author:  Mohi Syed
Date:    11/15/20
Section: 34
E-mail:  msyed2@umbc.edu
Description:
  plays the game of ur
"""


class RoyalGameOfUr:
    STARTING_PIECES = 7

    def __init__(self, board_file_name):
        self.board = None
        self.load_board(board_file_name)
        self.white = "White"    # White constant
        self.black = "Black"    # Black Constant

        self.roll = None       # defines my roll

        self.white_piece_list = []     # appends the white pieces
        self.black_piece_list = []     # appends the black pieces

        self.white_entry = None        # creates the white entry piece
        self.black_entry = None        # creates the black entry piece

        self.my_ur_piece = None        # calls the board pieces from the list to move
        self.complete = False          # win condition

    def load_board(self, board_file_name):
        """
        This function takes a file name and loads the map, creating BoardSquare objects in a grid.

        :param board_file_name: the board file name
        :return: sets the self.board object within the class
        """

        import json
        try:
            with open(board_file_name) as board_file:
                board_json = json.loads(board_file.read())
                self.num_pieces = self.STARTING_PIECES
                self.board = []
                for x, row in enumerate(board_json):
                    self.board.append([])
                    for y, square in enumerate(row):
                        self.board[x].append(BoardSquare(x, y, entrance=square['entrance'], _exit=square['exit'],
                                                         rosette=square['rosette'], forbidden=square['forbidden']))

                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if board_json[i][j]['next_white']:
                            x, y = board_json[i][j]['next_white']
                            self.board[i][j].next_white = self.board[x][y]
                        if board_json[i][j]['next_black']:
                            x, y = board_json[i][j]['next_black']
                            self.board[i][j].next_black = self.board[x][y]
        except OSError:
            print('The file was unable to be opened. ')

    def draw_block(self, output, i, j, square):
        """
        Helper function for the display_board method
        :param output: the 2d output list of strings
        :param i: grid position row = i
        :param j: grid position col = j
        :param square: square information, should be a BoardSquare object
        """
        MAX_X = 8
        MAX_Y = 5
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if x == 0 or y == 0 or x == MAX_X - 1 or y == MAX_Y - 1:
                    output[MAX_Y * i + y][MAX_X * j + x] = '+'
                if square.rosette and (y, x) in [(1, 1), (1, MAX_X - 2), (MAX_Y - 2, 1), (MAX_Y - 2, MAX_X - 2)]:
                    output[MAX_Y * i + y][MAX_X * j + x] = '*'
                if square.piece:
                    # print(square.piece.symbol)
                    output[MAX_Y * i + 2][MAX_X * j + 3: MAX_X * j + 5] = square.piece.symbol

    def display_board(self):
        """
        Draws the board contained in the self.board object
        """
        if self.board:
            output = [[' ' for _ in range(8 * len(self.board[i // 5]))] for i in range(5 * len(self.board))]
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if not self.board[i][j].forbidden:
                        self.draw_block(output, i, j, self.board[i][j])

            print('\n'.join(''.join(output[i]) for i in range(5 * len(self.board))))

    def roll_d4_dice(self, n=4):
        """
        Keep this function as is.  It ensures that we'll have the same runs with different random seeds for rolls.
        :param n: the number of tetrahedral d4 to roll, each with one dot on
        :return: the result of the four rolls.
        """
        dots = 0
        for _ in range(n):
            dots += choice([0, 1])
        return dots

    def find_entry_piece(self):        # find the entry pieces for the colors then appends
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].entrance == "White":        # checks to see "White"
                    self.white_entry = self.board[i][j]         # equates white entry it to self.board

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].entrance == "Black":        # checks to see "Black"
                    self.black_entry = self.board[i][j]         # equates black entry to self board

    def start_game(self):           # ask for the user input
        white_player_name = input("Whats your name? ")
        print(white_player_name, "You will be white")
        black_player_name = input("Whats your name? ")
        print(black_player_name, "You will be black")

    def create_pieces(self):             # creates pieces for the game
        for i in range(RoyalGameOfUr.STARTING_PIECES):
            white_ur_piece = UrPiece("White", "W{}".format(i), self.white_entry)        # calls ur piece and puts the white color and the symbol
            black_ur_piece = UrPiece("Black", "B{}".format(i), self.black_entry)        # calls ur piece and puts the black color and the symbol
            self.white_piece_list.append(white_ur_piece)                # appends the white and black pieces
            self.black_piece_list.append(black_ur_piece)

    def display_options(self, color):

        if color == self.white:                          # if its color white
            self.roll = self.roll_d4_dice(4)             # makes the roll already
            print("You have rolled a {}".format(self.roll))
            for i in range(len(self.white_piece_list)):  # fix
                if self.white_piece_list == type(str):        # check if anything in its not a string
                    print("{}.)    W{} currently off the board ".format(i + 1, i + 1))
                else:  # come back to add the postion part
                    print(self.white_piece_list[i], print(" ", BoardSquare.position))
        else:
            self.roll = self.roll_d4_dice(4)
            print("You have rolled a {}".format(self.roll))
            for i in range(len(self.black_piece_list)):
                if self.white_piece_list == type(str):
                    print("{}.)     B{} currently off the board ".format(i + 1, i + 1))
                else:  # come back to add the postion part
                    print(self.black_piece_list[i], print(" ", BoardSquare.position))

    def user_turn(self, color):
        if self.roll == 0:           # if roll is 0 then lose roll
            print(self.roll)
            print("lose turn")
        else:
            print(self.roll)
            if color == self.white:       # for white
                user_turn = int(input("What do you want to do? "))
                if user_turn == 1:
                    self.my_ur_piece = self.white_piece_list[0]        # makes myurpiece = to part of the white piece list

                if user_turn == 2:
                    self.my_ur_piece = self.white_piece_list[1]

                if user_turn == 3:
                    self.my_ur_piece = self.white_piece_list[2]

                if user_turn == 4:
                    self.my_ur_piece = self.white_piece_list[3]

                if user_turn == 5:
                    self.my_ur_piece = self.white_piece_list[4]

                if user_turn == 6:
                    self.my_ur_piece = self.white_piece_list[5]

                if user_turn == 7:
                    self.my_ur_piece = self.white_piece_list[6]

            else:           # for black
                user_turn = int(input("What do you want to do? "))
                if user_turn == 1:
                    self.my_ur_piece = self.black_piece_list[0]          # makes myurpiece = to part of the black piece list

                if user_turn == 2:
                    self.my_ur_piece = self.black_piece_list[1]

                if user_turn == 3:
                    self.my_ur_piece = self.black_piece_list[2]

                if user_turn == 4:
                    self.my_ur_piece = self.black_piece_list[3]

                if user_turn == 5:
                    self.my_ur_piece = self.black_piece_list[4]

                if user_turn == 6:
                    self.my_ur_piece = self.black_piece_list[5]

                if user_turn == 7:
                    self.my_ur_piece = self.black_piece_list[6]

    def move_piece(self, piece_to_move, dice_roll, color):
        if color == self.white:                         # color = white
            piece_to_move.position = self.white_entry         # position equals the entrance point
            dice_roll -= 1                               # takes 1 out of the steps

            piece_to_move.position.piece = None            # clears the previous part

            for i in range(dice_roll):                    # for the length of the dice roll
                piece_to_move.position = piece_to_move.position.next_white       # move to the next whtie spot
            piece_to_move.position.piece = piece_to_move                   # return back to normal
        else:        # for black
            piece_to_move.position = self.black_entry
            dice_roll -= 1

            piece_to_move.position.piece = None

            for i in range(dice_roll):
                piece_to_move.position = piece_to_move.position.next_black
            piece_to_move.position.piece = piece_to_move

    def done(self):  # was gonan check if done
        print()     # iterate through to check if all pieces of board

    def play_game(self):
        """
            Your job is to recode this function to play the game.
        """
        color = self.white       # temp variable changes
        self.start_game()
        self.find_entry_piece()
        self.create_pieces()
        while not self.complete:       # while game is not complete
            if color == self.white:
                self.display_board()
                self.display_options(color)
                self.user_turn(color)
                self.move_piece(self.my_ur_piece, self.roll, color)
                color = self.black
            else:
                self.display_board()
                self.display_options(color)
                self.user_turn(color)
                self.move_piece(self.my_ur_piece, self.roll, color)
                color = self.white


if __name__ == '__main__':
    file_name = input('What is the file name of the board json? ') if len(argv) < 2 else argv[1]
    rgu = RoyalGameOfUr(file_name)
    rgu.play_game()
