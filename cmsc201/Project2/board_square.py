"""
File:   board_Sqaure.py
Author:  mohi syed
Date:    11/15/20
Section: 34
E-mail:  msyed2@umbc.edu
Description:
  creates urs pieces and checks whehter or not the piece can move
"""


class UrPiece:
    def __init__(self, color, symbol, starting_position):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol
        self.starting_position = starting_position

        self.white = "White"

    def can_move(self, num_moves, color):
        if not self.complete:
            if color == self.white:
                a_board_square = self.position
                if not self.position:
                    a_board_square = self.starting_position
                    num_moves = num_moves - 1
                else:
                    a_board_square = self.position
                for i in range(num_moves):
                    a_board_square = a_board_square.next_white
                if BoardSquare.piece is not None:
                    if BoardSquare.piece.color != self.white:
                        if BoardSquare.rosette:
                            print("not a rosette")
                        else:
                            print("is a rosette cant move")
                    else:
                        print("cant move")
                if BoardSquare.next_white is None:
                    print("done")
                    self.complete = True
            else:
                a_board_square = self.position
                if not self.position:
                    a_board_square = self.starting_position
                    num_moves = num_moves - 1
                else:
                    a_board_square = self.position
                for i in range(num_moves):
                    a_board_square = a_board_square.next_black
                if BoardSquare.piece is not None:
                    if BoardSquare.piece.color != self.black:
                        if BoardSquare.rosette:
                            print("not a rosette")
                        else:
                            print("is a rosette cant move")
                    else:
                        print("cant move")
                if BoardSquare.next_black:
                    self.complete = True


class BoardSquare:

    def __init__(self, x, y, entrance=False, _exit=False, rosette=False, forbidden=False):
        self.piece = None
        self.position = (x, y)
        self.next_white = None
        self.next_black = None
        self.exit = _exit
        self.entrance = entrance
        self.rosette = rosette
        self.forbidden = forbidden

    def load_from_json(self, json_string):
        import json
        loaded_position = json.loads(json_string)
        self.piece = None
        self.position = loaded_position['position']
        self.next_white = loaded_position['next_white']
        self.next_black = loaded_position['next_black']
        self.exit = loaded_position['exit']
        self.entrance = loaded_position['entrance']
        self.rosette = loaded_position['rosette']
        self.forbidden = loaded_position['forbidden']

    def jsonify(self):
        next_white = self.next_white.position if self.next_white else None
        next_black = self.next_black.position if self.next_black else None
        return {'position': self.position, 'next_white': next_white, 'next_black': next_black, 'exit': self.exit,
                'entrance': self.entrance, 'rosette': self.rosette, 'forbidden': self.forbidden}
