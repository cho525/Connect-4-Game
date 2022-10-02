# Playing the game

from game_board import Board
from player import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board



#function 1
def process_move(p, b):
    """function takes two parameters: a Player object p for the player 
       whose move is being processed, and a Board object b for the 
       board on which the game is being played
    """
    print(str(p) + "'s turn")
    next_move = p.next_move(b)
    b.add_checker(p.checker,next_move)
    print()
    print(b)
    if b.is_win_for(p.checker):
        print()
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return True
    if b.is_full():
        print()
        print("It's a tie!")
        return True
    else:
        print()
        return False


#TESTCASES
#connect_four(Player('X'), Player('O'))
#When update to the new verison of spyder, 
#I can no longer play with another real player. 
#Kept saying spyder have counter an internal problem
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    