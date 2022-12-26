"""
A Teriffic Sudoku Application. 
This involves a player who must figure out how to input correctly the figures in each row, column and 3x3 box.

@author: Souad Yakubu(sny2)
@author: Edom Maru (eam43)
@date: Fall, 2022 
"""

from random import randint

class Sudoku:
    '''each row, column and square (3x3 grid) needs to be filled out
        with the numbers 1-9,without repeating any numbers within the row,
        column or square.'''
    
    def __init__(self):
        ''' Creates a 2 dimentional list with initial values equal to 0'''
        
        self.grid = []
        for x in range(0,9):
            self.grid.append([])
            for y in range(0,9):
                self.grid[x].append(0)
                
        self.get_data(self.random())
    def random(self):
        ''' chooses a file name'''
        puzzle=randint(1,4)
        puzzlefile = f'sudoku{puzzle}.txt'
        return puzzlefile
        
    
    def check(self):
        '''Checks if the input of the user is right or wrong accoding to the rules of the game using boolean values
            if ANY of these return False, then return False.
            if ALL of them return True, then return True'''
        for row in range(0,9):
            if self.check_answer(row) ==False:
                return False
        for column in range(0,9):
            if self.column_answer(column)==False:
                return False
        for box in range (0,9):
            if self.box_answer(box)== False:
                return False
        return True
        
    
    
    def get_data(self,puzzlefile):
        '''reads and opens different sudoku games from  a text file at random pick'''
        # The sudoku puzzle was taken from Professor Vander Linden
        #puzzle=randint(2,3)
        #puzzlefile = f'sudoku{puzzle}.txt'
        with open(puzzlefile) as f:
            lines = f.readline()
            ingrid=lines.split(',')
            for i in range(0,81):
                self.grid[i//9][i%9]=int(ingrid[i])
                
    
    def check_answer(self,row):
        '''checks if the answer in each row of the game has been correctly inputted
            and returns a boolean value
        '''
        #creates a list of nine False 
        check_list = [False]*9
        for i in range(len(check_list)):
            if self.grid[row][i] == 0:
                return False
            elif check_list[self.grid[row][i]-1] == True:
                return False
            else:
                check_list[self.grid[row][i]-1] = True
        return True
            
    def column_answer(self,column):
        '''checks if the answer in each column of the game has been correctly inputted
            and returns a boolean value
        '''
        check_list = [False]*9
        for i in range(len(check_list)):
            if self.grid[i][column] == 0:
                return False
            elif check_list[self.grid[i][column]-1]:
                return False
            else:
                check_list[self.grid[i][column]-1] = True
        return True
    
    def box_answer(self,boxnum):
        '''checks if the answer in each 3x3 grid of the game has been correctly inputted
            and returns a boolean value
        '''
        check_list = [False]*9
        
        if  boxnum == 0:
            for x in range (0,3):
                for y in range (0,3):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
                    
        if boxnum == 1:
            for x in range (3,6):
                for y in range (0,3):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
                
            
        if boxnum == 2:
            for x in range (6,9):
                for y in range (0,3):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
                    
        
        if boxnum == 3:
            for x in range (0,3):
                for y in range (3,6):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
        if boxnum == 4:
            for x in range (3,6):
                for y in range (3,6):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
        if boxnum == 5:
            for x in range (6,9):
                for y in range (3,6):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
        if boxnum == 6:
            for x in range (3,6):
                for y in range (6,9):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
        if boxnum == 7:
            for x in range (3,6):
                for y in range (6,9):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
        if boxnum == 8:
            for x in range (6,9):
                for y in range (6,9):
                    if self.grid[x][y] == 0:
                        return False
                    elif check_list[self.grid[x][y]-1]:
                        return False
                    else:
                        check_list[self.grid[x][y]-1] = True
                
        return True

if __name__ == "__main__":
    g = Sudoku()


