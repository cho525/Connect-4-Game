# An RandomPlayer for use in Connect Four


import random
from start_game import *  
from game_board import *
from player import *

class RandomPlayer(Player): 
    """An Random Player for the connect four game
    """
    def next_move(self, board):
        column=[]
        for i in range(board.width):
            if board.can_add_to(i) == True:
                column += [i]
        return random.choice(column)
    


#TESTCASE
#connect_four(RandomPlayer('X'), RandomPlayer('O'))




