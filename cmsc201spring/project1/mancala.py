"""
File:    mancala.py
Author:  Mohi Syed
Date:    4/9/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
	Plays the game of mancala
"""
  

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are 2d lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be 2d lists of strings.  Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def top_cup():     # initialized the top list
    top_player1 = []
    stones_list = [4, 4, 4, 4, 4, 4]        # intial stones
    for i in range(6):    # outer 2d list
        inital_cup = []
        for x in range(1):  # inner 2d list
            inital_cup.append("cup".ljust(BLOCK_WIDTH))
            inital_cup.append(str(i + 1))
            inital_cup.append("stones")
            inital_cup.append(str(stones_list[i]))
            inital_cup.append("")
        top_player1.append(inital_cup)
    return top_player1    # return the top list


def bottom_cup():
    bottom_player2 = []      #
    stones_list = [4, 4, 4, 4, 4, 4]
    for i in range(6):      # outer 2d list
        inital_cup = []
        for x in range(1):   # inner 2d list
            inital_cup.append("cup".ljust(BLOCK_WIDTH))
            inital_cup.append(str(13 - i))
            inital_cup.append("stones")
            inital_cup.append(str(stones_list[i]))
            inital_cup.append("")
        bottom_player2.append(inital_cup)

    return bottom_player2      # return the bottom list


def mancala_cup(player_names):
    mancala_list = []     # the mancala list

    for i in range(2 * BLOCK_HEIGHT + 1):
        if i == 3:
            mancala_list.append(f'{player_names}'.ljust(BLOCK_WIDTH))
        elif i == 7:
            mancala_list.append("stones")
        elif i == 8:
            mancala_list.append("0" + " " * (BLOCK_WIDTH - 1))
        else:
            mancala_list.append('     ')

    return mancala_list


def get_player():
    player_names = []
    user_input1 = input("Name of Player 1? ")         # input player 1
    player_names.append(user_input1)
    user_input2 = input("name of player 2? ")       # input player 2
    player_names.append(user_input2)
    return player_names


def user_input(player_name):
    player_input = int(input(f"{player_name} What cup do you want to move? "))
    number_list = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13]     # cups that are not mancala

    if type(player_input) == int:      # checking the type to see if it is not a string
        if player_input in number_list:      # if in the list
            return player_input
        if player_input == 0 or 7:     #  if its in mancala spot
            print("Cant move Mancala")
            return False


def move_cup(user_input, top_cup, bot_cup, mancala1, mancala2):
    # top_cup[]
    # 4th spot or 3rd index in the 2d top list is the stone value
    num = 0

    if 0 < user_input <= 6:      # check if its in top cup
        user_input -= 1  # cause of list index that starts at zero
        num = int(top_cup[user_input][3])             # make it a counter
        top_cup[user_input][3] = " " * (BLOCK_WIDTH - 1) + "0"
    elif 8 <= user_input <= 13:         # it its in bottom list
        user_input -= 1
        num = int(bot_cup[2 * BLOCK_WIDTH - user_input][3])
        bot_cup[2 * BLOCK_WIDTH - user_input][3] = " " * (BLOCK_WIDTH - 1) + "0"    # change to zero

    for i in range(num):      # now we moving the pieces around
        temp_postion = user_input + i + 1        # temp postion
        if temp_postion < 6:
            str_num = str(int(top_cup[temp_postion][3]) + 1)       # top cup
            top_cup[temp_postion][3] = " " * (BLOCK_WIDTH - len(str_num)) + str_num     # add plus one
        elif temp_postion == 6:    # mancala spot for player 1
            str_num = str(int(mancala2[8]) + 1)     # add plus one
            mancala2[8] = str_num + " " * (BLOCK_WIDTH - len(str_num))      # actually change it
        elif 7 <= temp_postion < 13:     # bottom piece
            str_num = str(int(bot_cup[2 * BLOCK_WIDTH - temp_postion][3]) + 1)
            bot_cup[2 * BLOCK_WIDTH - temp_postion][3] = " " * (BLOCK_WIDTH - len(str_num)) + str_num
        elif temp_postion == 13:   # player 2 piece
            str_num = str(int(mancala1[8]) + 1)
            mancala1[8] = str_num + " " * (BLOCK_WIDTH - len(str_num))


def take_turn(player, turn, top, bot, mancala1, mancala2):
    if turn % 2 == 0:    # moduluo to check if its even if not it will go to player 2
        players = player[0]
    elif turn % 2 == 1:
        players = player[1]
    draw_board(top, bot, mancala1, mancala2)    # draw the board
    move_cup(user_input(players), top, bot, mancala1, mancala2)   # move the cup


def run_game():
    player_turn = 0      # intiallize the cup
    player_name = get_player()       # intiallze the name
    game_end = False    # winning conditon
    bot = bottom_cup()    # bot cup
    top = top_cup()    # top cup
    mancala1 = mancala_cup(player_name[0])   # player 1 mancala
    mancala2 = mancala_cup(player_name[1])  # player 2 mancala

    while not game_end:    # game loop
        if player_turn % 2 == 0:    # player 1 turn
            take_turn(player_name, player_turn, top, bot, mancala1, mancala2)
            if mancala1[8] >= str(5):    # if its == to five then end game
                print("{} has won the game ".format(player_name[0]))
                game_end = True
            player_turn += 1  # change turn
        elif player_turn % 2 == 1:   # player 2 turn
            take_turn(player_name, player_turn, top, bot, mancala1, mancala2)
            if mancala2[8] >= str(5): # if its == to five then end game
                print("{} has won the game ".format(player_name[0]))
                game_end = True
            player_turn += 1



if __name__ == "__main__":
    run_game()
