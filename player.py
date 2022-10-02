# A Connect Four Player class 


from game_board import Board



class Player:
    """a data type for players playing connect four
    """
    

    def __init__(self, checker):
        """function constructs a new Player object by initializing the 
           following two attributes
        """
        assert(checker == 'X' or checker == 'O')    
        self.checker = checker
        self.num_moves = 0
        
        

    def __repr__(self):
        """function returns a string representing a Player object 
           The string returned should indicate which checker 
           the Player object is using
        """
        s='Player'+' '+(self.checker)
        
        return s
    
    


    def opponent_checker(self):
        """function returns a one-character string representing the 
           checker of the Player object’s opponent
        """
        if self.checker=='X':
            return 'O'
        else:
            return 'X'
   
        

    def next_move(self, b):
        """function returns the column where the player wants to 
           make the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col):
                 return col
            else:
                 print('Try again!')
        
        
        
        
        
        
        
        
        
        
        
        
