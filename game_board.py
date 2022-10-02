# Connect Four Game



class Board:
    """A data type for a connect four board with arbitary dimensions
    """
    

    def __init__(self, height, width):
        """a constructor for board objects
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        

        

    def __repr__(self):
        """function returns a string representing a Board object
        """
        s = ''
        
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  
        for line in range(self.width * 2 + 1):
            s += '-'
        s += '\n'
        for num in range(self.width):
            s += ' ' + str((num) % 10)
        
            
        return s
    




    def add_checker(self, checker, col):
        """funciton will add a checker into the Board
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        row = 0
        while self.slots[row][col] == ' ': 
            row += 1
            if row == self.height - 1:
                break
        if self.slots[row][col] != ' ':
            row += -1
            
        self.slots[row][col] = checker
        
          
            

                
    def reset(self):
        """function will reset the board
        """
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '


    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object 
            starting with 'X' 
        """
        
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self, col):
        """function returns True if it is valid to place a checker 
           in the column col on the calling Board object
           Otherwise it should return False
        """
        if col < 0:
            return False
        elif col > self.width - 1:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True


    def is_full(self):
        """returns True if the called Board object is completely full 
           of checkers, and returns False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
            else:
                return True
        


    def remove_checker(self, col):
        """function removes the top checker from the column
           if the colmun is empty the function should do nothing
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return



#helper function for is_win_for
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                            self.slots[row][col + 3] == checker:
                                return True

    
        return False



    def is_vertical_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                            self.slots[row + 3][col] == checker:
                                return True

    
        return False



    def is_up_diagonal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                            self.slots[row - 3][col + 3] == checker:
                                return True

    
        return False



    def is_down_diagonal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                            self.slots[row + 3][col + 3] == checker:
                                return True

    
        return False









#function is_win_for
    def is_win_for(self, checker):
        """function returns True if there are four consecutive slots 
           containing checker on the board Otherwise it should return False
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_down_diagonal_win(checker) == True:
            return True
        if self.is_up_diagonal_win(checker) == True:
            return True
        if self.is_vertical_win(checker) == True:
            return True
        if self.is_horizontal_win(checker) == True:
            return True
        return False
        
                        
        
            
        
        
            
        
            
        
        
        
        
                
            
                
                
                
                
                
            
       
        
        
        
        


