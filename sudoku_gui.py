"""
A GUI controller for a Sudoku game.
@author: Edom Maru(eam43)
@author: Souad Yakubu(sny2)
@date: Fall, 2022

"""
from guizero import App, Text, PushButton, Box,Drawing , Window,TextBox
from SUDOKU import Sudoku
from timer import Timer
class SodukuApp:
    
    def __init__(self, app):
        '''Initializes variables and calls method in an orderly manner'''
        self.cell_width = 9
        self.SUDOKU = Sudoku()
        
        #Arranges the application GUI.
        app.title = 'Sudoku'
        app.width = 1000 #using fixed width/height
        app.height = 1000
        app.font = 'Times new roman'
        app.text_size = 20
        
        #sets a window to display the game instructions 
        self.startscreen=Window(app,title='instructions',height=500, width=650)
        self.instructions()
        
        # makes a master application box to grid the layout 
        self.appbox = Box(app, layout='grid',width=1000,height=1000)
        
        #makes and positions the text and boxes used
        self.timebox=Box(self.appbox, layout='grid',grid=[0,0], width=700,height=40,align="left")
        self.title=Text(self.timebox, grid=[0,0],text='SUDOKU',width=30, size = 30)
        self.timertext=Text(self.timebox, grid=[1,0],text='Timer:',width=5)
        self.time=Text(self.timebox, grid=[2,0],text='')
        
        self.timer=Timer()
        self.update_clock()
        app.repeat(1000, self.update_clock)
        
        # makes the main gamebox for all the pushbuttons
        self.gamebox = Box(self.appbox, layout='grid', grid=[0,1], width=820, height=820)
        self.setup()
        
        Box(self.appbox, width=720, height=20,grid=[0,2])
        # makes the bottom buttons for reset and quit
        self.buttonbox=Box(self.appbox, layout='grid', grid=[0,3], width=700, height=60)
        self.title=PushButton(self.buttonbox, grid=[0,0],text='RESET', height=1, command=self.setup)
        self.title.text_size=12
        self.quit=PushButton(self.buttonbox, grid=[1,0], text='QUIT', height=1, command=app.destroy)
        self.quit.text_size=12
        
        #provides the status of the game
        self.status=Text(self.buttonbox,grid=[2,0], text='     Status: Not Completed', size = 21)
        
        app.when_key_pressed=self.process_key_event
        
        
    def update_clock(self):
        '''Updates the value of the time on the gui app'''
        self.time.value = '{:.0f}.0 s'.format(self.timer.get_time()) # This was line was taken from timer.py
        if int(self.timer.get_time()) >= 600 and int(self.timer.get_time())<601:
            app.disable()
            self.hangman()
            #self.timer = False

            
    def checking(self):
        '''changes the status of the game after the game is correctly computed'''
        if self.game.check() == True:
            self.status.value ='Status: Congratulation you did it!'
        else:
            print('Not done yet')
       
    def processmouse(self,x,y):
        ''' Receives and initializes the positions x and y'''
        #print(x,y)
        self.x=x
        self.y=y
    

    def process_key_event(self,event):
        ''' Processes and stores the value of the keys '''
        if event.key=='1':
            self.buttons[self.x][self.y].text = '1'
            self.game.grid[self.x][self.y]= 1
        elif event.key == '2':
            self.buttons[self.x][self.y].text = '2'
            self.game.grid[self.x][self.y]= 2
        elif event.key =='3':
            self.buttons[self.x][self.y].text = '3'
            self.game.grid[self.x][self.y]= 3
        elif event.key == '4':
            self.buttons[self.x][self.y].text = '4'
            self.game.grid[self.x][self.y]= 4
        elif event.key == '5':
            self.buttons[self.x][self.y].text = '5'
            self.game.grid[self.x][self.y]= 5
        elif event.key =='6':
            self.buttons[self.x][self.y].text = '6'
            self.game.grid[self.x][self.y]= 6
        elif event.key == '7':
            self.buttons[self.x][self.y].text = '7'
            self.game.grid[self.x][self.y]= 7
        elif event.key == '8':
            self.buttons[self.x][self.y].text = '8'
            self.game.grid[self.x][self.y]= 8
        elif event.key =='9':
            self.buttons[self.x][self.y].text = '9'
            self.game.grid[self.x][self.y]= 9
       
        self.checking()# called from the game to check if the input was correct 
                
    def setup(self):
        '''Sets up and initializes a 9X9 Sudoku game '''
        self.buttons = []

        self.game = Sudoku()
        # cleanup old buttons if necessary
        if(len(self.buttons) > 0):
            for x in range(0,9):
                for y in range(0,9):
                    self.buttons[x][y].destroy()
            self.buttons = []
        
        
        # makes buttons from game grid
        #some idea from the tictaktoe game 
        for x in range(0,9):
            self.buttons.append([])
            for y in range(0,9):
                if self.game.grid[x][y] != 0:
                    self.button = PushButton(self.gamebox, command=self.processmouse, args=[x,y],enabled=False,
                                width=3, height=1,
                                grid=[x,y],
                                text=self.game.grid[x][y]
                                )
                else:
                    self.button = PushButton(self.gamebox, command=self.processmouse, args=[x,y],
                                width=3, height=1,
                                grid=[x,y],
                                text = ''
                                )
                self.buttons[x].append(self.button)
                
        
        
        #loops through and passes boxnums to the colors method
        for boxnum in range(0,9):
            self.colors(boxnum)
            
    def colors(self,boxnum):
        '''Changes the colors of each 3x3 boxes'''
        if  boxnum == 0:
            for x in range (0,3):
                for y in range (0,3):
                    self.buttons[x][y].bg='cyan'
        if boxnum == 1:
            for x in range (3,6):
                for y in range (0,3):
                    self.buttons[x][y].bg='white'
        if boxnum == 2:
            for x in range (6,9):
                for y in range (0,3):
                    self.buttons[x][y].bg='cyan'
        if boxnum == 3:
            for x in range (0,3):
                for y in range (3,6):
                    self.buttons[x][y].bg='white'
        if boxnum == 4:
            for x in range (3,6):
                for y in range (3,6):
                    self.buttons[x][y].bg='cyan'
        if boxnum == 5:
            for x in range (6,9):
                for y in range (3,6):
                    self.buttons[x][y].bg='white'
        if boxnum == 6:
            for x in range (0,3):
                for y in range (6,9):
                    self.buttons[x][y].bg='cyan'
        if boxnum == 7:
            for x in range (3,6):
                for y in range (6,9):
                    self.buttons[x][y].bg='white'
        if boxnum == 8:
            for x in range (6,9):
                for y in range (6,9):
                    self.buttons[x][y].bg='cyan'
                    
    def instructions(self):
        '''reads and displays the instructions of the game from a text file into a window'''
        self.instruction=Text(self.startscreen, text = 'INSTRUCTIONS',font='Times new roman', color='Red',size=30)
        with open("Instruction.txt") as f:
            lines = f.readlines()
            for line in lines:
                line.strip('\n')
                self.inst=Text(self.startscreen, text=line, size =13,font='Times new roman')

                    
    
    def hangman(self):
        '''draws hangman for the game when time is up
            it is called in the  time'''
        
        self.window2=Window(app,title='hangman', height=400,width=400)
        Text(self.window2,text='Muhahaha! \n  Game over! \n You were killed!', align ='left')
        drawing=Drawing(self.window2,width=400,height=400)
        
        #draws hangman stick
        drawing.line(50,50,100,50)
        drawing.line(100,50,100,300)
        drawing.line(50,50,50,100)
        drawing.line(75,300,125,300)
        #draws face
        drawing.oval(25,100,75,150, color='red', outline=True,outline_color='black')
        # draws body
        drawing.line(50,150,50,250)
        #draws arms
        drawing.line(50,175,25,200)
        drawing.line(50,175,75,200)
        #draws legs
        drawing.line(50,250,25,275)
        drawing.line(50,250,75,275)



if __name__ == '__main__':
    app = App()
    SodukuApp(app)
    app.display()