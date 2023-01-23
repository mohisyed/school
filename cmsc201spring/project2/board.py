"""
File:    board.py
Author:  Mohiuddin Syed
Date:    4/25/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:    This is board class for battleship game.
"""
# the contants for empty, hit and miss element of board
EMPTY_STRING = "  "
MISS_STRING = "O "
HIT_STRING = "X "
# the contants for result after shot
WIN_STRING = "win"
SUNK_STRING = "sunk"
AGAIN_STRING = "again"


class Board:
    def __init__(self, size):
        """
        The constructor
        :param self
        """
        # creaet a size x size board
        self.size = size
        # player board list_2d
        self.player_board = []
        # the target board list_2d
        self.target_board = []

        # the dict to contain the status of the ship
        # ex: ["Carrier", 5]: 5 is the number of ship pieces
        # if 5 go to 0 the ship has sunk
        self.ship_dict = {
            "Ca": ["Carrier", 5],
            "Ba": ["Battleship", 4],
            "Cr": ["Cruiser", 3],
            "Su": ["Submarine", 3],
            "De": ["Destroyer", 2]
        }

        # set all place of board to empty
        for i in range(0, size):
            self.player_board.append([EMPTY_STRING] * size)
            self.target_board.append([EMPTY_STRING] * size)

    def register_shot(self, x, y):
        """
        A function to return the status of the shot
        and update player board
        return AGAIN_STRING to announce player need to shot again
        return MISS_STRING to announce player miss
        return HIT_STRING to announce player hit
        return SUNK_STRING to announce player sunk a ship
        return WIN_STRING to announce player give the shot win
        :param self
        :param x, y: x, y coordinates to check the shot
        """
        # check if the shot is out of range
        if x < 0 or y < 0 or x >= self.size or y >= self.size:
            print("Shot coordinates are out of range, try again")
            return AGAIN_STRING
        # check if the shot has been shot before
        elif self.player_board[y][x] == HIT_STRING \
                or self.player_board[y][x] == MISS_STRING:
            print("Space has been shot before, try again")
            return AGAIN_STRING
        # if the place is empty, print miss and update player board
        elif self.player_board[y][x] == EMPTY_STRING:
            self.player_board[y][x] = MISS_STRING
            print("You miss.")
            return MISS_STRING
        # if the place is hit
        else:
            # get the name of the ship has been hit
            hit_name = self.player_board[y][x]
            # update the player board
            self.player_board[y][x] = HIT_STRING

            # go throughout all the ship in dict
            # to check the ship sank and player alive
            for ship in self.ship_dict.keys():
                # if the ship is same name with hit ship,
                # reduce the piece number of the hit ship
                if ship == hit_name:
                    # reduce piece number
                    self.ship_dict[ship][1] -= 1
                    # if piece number = 0, the ship has sunk
                    if self.ship_dict[ship][1] == 0:
                        # remove the ship from the dict
                        self.ship_dict.pop(ship)
                        # if number of ship in dict = 0,
                        # the player give the shot win
                        if len(self.ship_dict) == 0:
                            return WIN_STRING
                        # if there are still ship alive,
                        # only announce a ship has sunk
                        else:
                            print("You sunk a opponent ship")
                            return SUNK_STRING
            # if ship not sunk, only announce the ship got hit
            print("You hit a opponent ship.")
            return HIT_STRING

    def get_board(self, active_board):
        """
        A function to return board
        :param active_board: bool param if True return player Board
                            if False return the target Board
        """
        if active_board:
            return self.player_board
        elif not active_board:
            return self.target_board

    def place_ship(self, ship, start_pos, end_pos):
        """
        A function to place the ship on player board and return the status
        return true if placing successful
        return false if placing fail
        :param ship: short name of the ship
        :param start_pos: the list of x, y start position
        :param end_pos: the list of x, y end position
        """
        # check if start pos is negative
        if start_pos[0] < 0 or start_pos[1] < 0:
            print("Invalid position or overlapping ships, try again")
            return False
        # check if end pos is over the size of the board
        if end_pos[0] >= self.size or end_pos[1] >= self.size:
            print("Invalid position or overlapping ships, try again")
            return False
        # go from start_pos to end_pos check if overlapping ships
        for x in range(start_pos[0], end_pos[0] + 1):
            for y in range(start_pos[1], end_pos[1] + 1):
                # if the place is empty,
                if self.player_board[y][x] != EMPTY_STRING:
                    print("Invalid position or overlapping ships, try again")
                    return False
        # if all is ok,
        # go from start_pos to end_pos placing the ship on board
        for x in range(start_pos[0], end_pos[0] + 1):
            for y in range(start_pos[1], end_pos[1] + 1):
                self.player_board[y][x] = ship
        # show the player board after placing successful
        self.display_board(True)
        # return true when placing successful
        return True

    def display_board(self, active_board):
        """
        A function to print the board to screen
        :param active_board: the bool to choose which board to print
                    if True print player Board
                    if False print target Board
        """
        # get the board
        grid = self.get_board(active_board)
        # print the spaces for row index line
        print("  ", end="")
        # print row index line number
        for i in range(0, self.size):
            print("{:<3}".format(i), end="")
        # end of the row index line
        print("\n", end="")

        # count is column index number
        count = 0
        # print the column index and the board element
        for row in grid:
            # print column index
            print("{:<2}".format(count), end="")
            # print the element
            print("|".join(row), end="")
            # print the last | at the end of line
            print("|")
            count += 1
