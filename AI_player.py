# An AI Player for use in Connect Four


import random
from player import *
from game_board import *
from start_game import * 


class AIPlayer(Player):
    """an AI player
    """

#init constructor    
    def __init__(self, checker, tiebreak, lookahead):
        """function constructs a new AIPlayer object
        """
        assert(checker == 'O' or checker == 'X')
        assert(tiebreak == 'RIGHT' or tiebreak == 'LEFT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
    
        Player.__init__(self, checker)  
        self.tiebreak = tiebreak
        self.lookahead = lookahead

#repr method    
    def __repr__(self): 
        """returns a string representing an AIPlayer
        """
        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')')


#max score method
    def max_score_column(self, scores):
        ''' takes a list scores containing a score for each column of the board
        and returns the index of the column with the maximum score. Applies
        tiebreaking strategy to break any ties
        '''
        max_scores = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_scores += [i]
        if self.tiebreak == 'LEFT':
            return max_scores[0]
        if self.tiebreak == 'RIGHT':
            return max_scores[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(max_scores)
    
        
#scores for method
    def scores_for(self, board):
        """ takes a Board and determines the called AIPlayer's
        scores for the columns in board
        """
        scores = [50] * len(range(board.width))

        for col in range(board.width):
            #checking to see if the column is full
            if not board.can_add_to(col):
                scores[col] = -1
            #checking to see if the next move wins the game for AI Player    
            elif board.is_win_for(self.checker):
                scores[col] = 100
            #checking to see if the next move will allow the opponent to win    
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0 :
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                other_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                other_scores = other_player.scores_for(board)
                if max(other_scores) == 0:
                    scores[col] = 100
                elif max(other_scores) == 100:
                    scores[col] = 0
                elif max(other_scores) == 50:
                    scores[col] = 50
                    
                board.remove_checker(col)
        return scores

#next move method    
    def next_move(self, board):
        """ returns the  AIPlayer's judgement of its best possible move
        """
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)

    


#TESTCASES BELOW

#connect_four(AIPlayer('X', 'LEFT', 0), AIPlayer('O', 'LEFT', 0))  
#('X or O', 'Strategy for tiebreak', 'Lookahead Moves')  
        
        
        
        