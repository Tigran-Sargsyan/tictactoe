from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
import sys
import random

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        # Geometry of the window
        self.setGeometry(500,100,462,570) 
        self.setMinimumSize(462,570)
        self.setMaximumSize(462,570)

        self.counter = 0  # A counter to determine whose move it is
        self.flag = True  # A flag to tell if a game is still in process
        self.game_mode = 0 # A variable for holding the mode of the game (1: 2Player, 2:vs Computer)

        self.lst = list(range(9)) # Defining a list with values [0,8] for storing X-s and O-s 
        
        self.win_lst = [] # Defining a list to hold the winning squares

        # Counting how many times has each player won for showing it in the interface
        self.winX = 0
        self.winY = 0

        self.initUI() # A function for the UI of the window

    def initUI(self):
        """Creating buttons,setting geometry,text in the buttons,styling"""

        self.btn1 = QtWidgets.QPushButton(self) # btn1 to btn9 are the squares of the playing board
        self.btn1.setGeometry(5,10,150,100)
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(156,10,150,100)
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(307,10,150,100)
        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setGeometry(5,111,150,100)
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setGeometry(156,111,150,100)
        self.btn6 = QtWidgets.QPushButton(self)
        self.btn6.setGeometry(307,111,150,100)
        self.btn7 = QtWidgets.QPushButton(self)
        self.btn7.setGeometry(5,212,150,100)
        self.btn8 = QtWidgets.QPushButton(self)
        self.btn8.setGeometry(156,212,150,100)
        self.btn9 = QtWidgets.QPushButton(self)
        self.btn9.setGeometry(307,212,150,100)
        self.btn10 = QtWidgets.QPushButton(self)  # btn10 is clicked when the user wants to play again
        self.btn10.setGeometry(0,410,462,50)
        self.btn10.setText("Play again")
        self.btn10.setFont(QFont('Times', 30)) 
        self.mode1 = QtWidgets.QPushButton(self)
        self.mode1.setGeometry(0,470,150,60)
        self.mode1.setText("2 Player") # If the user wants 2 player mode
        self.mode1.setFont(QFont('Times', 20)) 
        self.mode2 = QtWidgets.QPushButton(self)
        self.mode2.setGeometry(312,470,150,60)
        self.mode2.setText("vs Computer") # If the user wants to play against the computer
        self.mode2.setFont(QFont('Times', 20))
        
        # Creating a list of buttons for further easier use
        self.button_list = [
            self.btn1,
            self.btn2,
            self.btn3,
            self.btn4,
            self.btn5,
            self.btn6,
            self.btn7,
            self.btn8,
            self.btn9
        ]

        # Setting the text and the size of the text of squares
        for button in self.button_list:
            button.setText("")
            button.setFont(QFont('Times', 30))

        self.label = QtWidgets.QLabel(self)  # Label to tell whose turn to play is at the moment
        self.label.setGeometry(350,330,120,60)
        self.label.setText("X's turn")
        self.label.setStyleSheet("QLabel{font-size: 30pt;}")
        self.player1 = QtWidgets.QLabel(self) # player1 and player2 labels store how many games has each player won
        self.player1.setGeometry(10,330,70,30)      
        self.player1.setText("Player1: ")
        self.player1.setStyleSheet("QLabel{font-size: 18pt;}")
        self.player2 = QtWidgets.QLabel(self)
        self.player2.setGeometry(10,370,70,30)
        self.player2.setText("Player2: ")
        self.player2.setStyleSheet("QLabel{font-size: 18pt;}")
        self.score_1 = QtWidgets.QLabel(self) # score1 and score2 for keeping the score
        self.score_1.setGeometry(75,339,15,15)
        self.score_1.setText("0")  
        self.score_1.setStyleSheet("QLabel{font-size: 18pt;}")
        self.score_2 = QtWidgets.QLabel(self)
        self.score_2.setGeometry(75,379,15,15)
        self.score_2.setText("0")
        self.score_2.setStyleSheet("QLabel{font-size: 18pt;}")

        # Styling
        self.setStyleSheet('background-color: #adc9c3;')
        self.btn1.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn2.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn3.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn4.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn5.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn6.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn7.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn8.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn9.setStyleSheet("QPushButton {color: #ff4747;}")
        self.btn10.setStyleSheet("background-color: #4b7173")

        # Clicking the buttons
        self.btn1.clicked.connect(lambda: self.click(self.btn1,0))
        self.btn2.clicked.connect(lambda: self.click(self.btn2,1))
        self.btn3.clicked.connect(lambda: self.click(self.btn3,2))
        self.btn4.clicked.connect(lambda: self.click(self.btn4,3))
        self.btn5.clicked.connect(lambda: self.click(self.btn5,4))
        self.btn6.clicked.connect(lambda: self.click(self.btn6,5))
        self.btn7.clicked.connect(lambda: self.click(self.btn7,6))
        self.btn8.clicked.connect(lambda: self.click(self.btn8,7))                
        self.btn9.clicked.connect(lambda: self.click(self.btn9,8))
        self.btn10.clicked.connect(self.reset)
        self.mode1.clicked.connect(lambda: self.mode(1))
        self.mode2.clicked.connect(lambda: self.mode(2))

    def mode(self,game_mode):
        """ A function to determine what mode the user wants to play in """
        self.game_mode = game_mode
        print(self.game_mode)
        self.mode1.deleteLater()
        self.mode2.deleteLater()
        if game_mode == 2: 
            self.random_list = list(range(9)) # For logic when playing with computer
       
    
    
    def click(self,btn,pos):
        """ A function that is invoked when buttons are clicked """
        if self.game_mode == 1:
            self.two_player(btn,pos) 
        elif self.game_mode == 2:
            self.vsCmp(btn,pos)    

    def two_player(self,btn,pos):
        """ A function that is invoked when the game is on 2player mode and a button in the board is clicked """
        if self.counter % 2 == 0:
            btn.setText("X")
            btn.setEnabled(False)
            self.label.setText("O's turn!")
            self.lst[pos]="X"
            self.win(self.lst,"X")
        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.label.setText("X's turn")
            self.lst[pos]="O"
            self.win(self.lst,"O")
    
        print(self.lst)
        self.counter += 1  # incrementing the counter after each move

    def vsCmp(self,btn,pos):
        """ A function that is invoked when the game is on vs Computer mode and a button in the board is clicked"""
        btn.setText("X")
        btn.setEnabled(False)
        self.label.setText("X's turn!")
        self.lst[pos]="X"
        self.random_list.remove(pos)
        self.win(self.lst,"X")
        print(self.lst)
        if self.flag:
            print(self.random_list,"random list before picking")
            if self.random_list:
                pick = random.choice(self.random_list)
                self.random_list.remove(pick)
                print(self.random_list,"random list after picking")
                eval(f"self.btn{pick+1}").setText("O") 
                eval(f"self.btn{pick+1}").setEnabled(False)
                self.lst[pick] = "O"
                self.win(self.lst,"O")      

    def win(self,lst,player):
        """ A function to check if the winning condition occured """
        if self.check_horizontal(lst) or self.check_vertical(lst) or self.check_diagonal(lst):
            self.label.setText(f"{player} won!")
            if player == "X":
                self.winX += 1
            else:
                self.winY += 1
            self.score_1.setText(f"{self.winX}")
            self.score_2.setText(f"{self.winY}")
            for i in range(3):
                eval(f"self.btn{str(self.win_lst[i]+1)}").setStyleSheet("QPushButton {color: #ff0000;}")
            for button in self.button_list:
                button.setEnabled(False)
            self.flag = False       

    def check_horizontal(self,lst):
        """ Subfunction of win() which checks horizontals """
        for i in range(3):
            if lst[i] == lst[i+3] == lst[i+6]:
                self.win_lst.extend([i,i+3,i+6])
                print(self.win_lst)
                return True

    def check_vertical(self,lst):
        """ Subfunction of win() which checks verticals """
        for i in range(0,7,3):
            if lst[i] == lst[i+1] == lst[i+2]:
                self.win_lst.extend([i,i+1,i+2])
                print(self.win_lst)
                return True

    def check_diagonal(self,lst):
        """ Subfunction of win() which checks diagonals """
        if lst[0] == lst[4] == lst[8]:
            self.win_lst.extend([0,4,8])
            print(self.win_lst)
            return True
        elif lst[2] == lst[4] == lst[6]:
            self.win_lst.extend([2,4,6])
            print(self.win_lst)
            return True    

    def reset(self):
        """ A function that resets all the elements in the game window """
        for button in self.button_list:
            button.setText("")
            button.setEnabled(True)

        self.lst = list(range(9))
        self.random_list = list(range(9))
        self.label.setText("X's turn")

        # Clearing and reseting
        if self.win_lst:
            for i in range(3):
                eval(f"self.btn{str(self.win_lst[i]+1)}").setStyleSheet("QPushButton {color: #ff4747;}")
        
        self.counter = 0
        self.win_lst = []
        self.flag = True


def start():
    app = QApplication(sys.argv)
    game_window = Window()
    game_window.show()
    app.exec_()

start()    
