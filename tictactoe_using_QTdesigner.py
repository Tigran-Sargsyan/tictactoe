from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        # Loading the ui file
        uic.loadUi("toe.ui", self) 
        
        # Changing the title of the window
        self.setWindowTitle("TicTacToe")

        self.game_mode = 0

        # Defining widgets
        self.button1 = self.findChild(QPushButton,"Button_1")
        self.button2 = self.findChild(QPushButton,"Button_2")
        self.button3 = self.findChild(QPushButton,"Button_3")
        self.button4 = self.findChild(QPushButton,"Button_4")
        self.button5 = self.findChild(QPushButton,"Button_5")
        self.button6 = self.findChild(QPushButton,"Button_6")
        self.button7 = self.findChild(QPushButton,"Button_7")
        self.button8 = self.findChild(QPushButton,"Button_8")
        self.button9 = self.findChild(QPushButton,"Button_9")
        self.button10 = self.findChild(QPushButton,"Button_10")
        self.mode1 = self.findChild(QPushButton,"mode1")
        self.mode2 = self.findChild(QPushButton,"mode2")
        self.label = self.findChild(QLabel,"label")
        self.player1 = self.findChild(QLabel,"player1")
        self.player2 = self.findChild(QLabel,"player2")

        # Styling
        self.setStyleSheet('background-color: #adc9c3;')
        self.button1.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button2.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button3.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button4.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button5.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button6.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button7.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button8.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button9.setStyleSheet("QPushButton {color: #ff4747;}")
        self.button10.setStyleSheet("background-color: #4b7173")

        # Showing the app
        self.show()

        # Clicking the button
        self.button1.clicked.connect(lambda: self.click(self.button1,0))  # The second parameter is button's corresponding place in the list
        self.button2.clicked.connect(lambda: self.click(self.button2,1))
        self.button3.clicked.connect(lambda: self.click(self.button3,2))
        self.button4.clicked.connect(lambda: self.click(self.button4,3))
        self.button5.clicked.connect(lambda: self.click(self.button5,4))
        self.button6.clicked.connect(lambda: self.click(self.button6,5))
        self.button7.clicked.connect(lambda: self.click(self.button7,6))
        self.button8.clicked.connect(lambda: self.click(self.button8,7))
        self.button9.clicked.connect(lambda: self.click(self.button9,8))
        self.mode1.clicked.connect(lambda: self.mode(1)) # Mode1: 2 Player
        self.mode2.clicked.connect(lambda: self.mode(2)) # Mode2: vs Computer
        self.button10.clicked.connect(self.reset)  # Invoking reset fucntion when 'Play again button' is clicked 

        # A list of all buttons
        self.button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9
        ]

        for button in self.button_list:
            button.setEnabled(False)

        self.counter = 0  # A counter to determine whose move it is
        self.flag = True  # A flag to tell if a game is still in process

        # Defining a list with values [0,8] for storing X-s and O-s 
        self.lst = list(range(9))

        # Defining a list to hold the winning squares
        self.win_lst = []

        # Counting how many times has each player won for showing it in the interface
        self.winX = 0
        self.winY = 0

    def mode(self,game_mode):
        self.game_mode = game_mode
        self.mode1.deleteLater()
        self.mode2.deleteLater()
        if game_mode == 2: 
            self.random_list = list(range(9)) # For logic when plaing with computer
        for button in self.button_list:
            button.setEnabled(True)    

    def click(self,btn,pos):
        #print(self.game_mode)
        if self.game_mode == 1:
            self.two_player(btn,pos) 
        elif self.game_mode == 2:
            self.vsCmp(btn,pos)    

    def two_player(self,btn,pos):
        if self.counter % 2 == 0:
            btn.setText("X")
            btn.setEnabled(False)
            self.label.setText("O's turn!")
            self.lst[pos]="X"
            self.win(self.lst,"X")
            print(self.lst)
        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.label.setText("X's turn")
            self.lst[pos]="O"
            self.win(self.lst,"O")
            print(self.lst)
        self.counter += 1  # incrementing the counter after each move

    def vsCmp(self,btn,pos):
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
                eval(f"self.button{pick+1}").setText("O")
                eval(f"self.button{pick+1}").setEnabled(False)
                self.lst[pick] = "O"
                self.win(self.lst,"O")      

    def win(self,lst,player):
        if self.check_horizontal(lst) or self.check_vertical(lst) or self.check_diagonal(lst):
            self.label.setText(f"{player} won!")
            if player == "X":
                self.winX += 1
            else:
                self.winY += 1
            self.player1.setText(f"{self.winX}")
            self.player2.setText(f"{self.winY}")
            for i in range(3):
                eval(f"self.button{str(self.win_lst[i]+1)}").setStyleSheet("QPushButton {color: #ff0000;}")
            for button in self.button_list:
                button.setEnabled(False)
            self.flag = False       

    def check_horizontal(self,lst):
        for i in range(3):
            if lst[i] == lst[i+3] == lst[i+6]:
                self.win_lst.extend([i,i+3,i+6])
                print(self.win_lst)
                return True

    def check_vertical(self,lst):
        for i in range(0,7,3):
            if lst[i] == lst[i+1] == lst[i+2]:
                self.win_lst.extend([i,i+1,i+2])
                print(self.win_lst)
                return True

    def check_diagonal(self,lst):
        if lst[0] == lst[4] == lst[8]:
            self.win_lst.extend([0,4,8])
            print(self.win_lst)
            return True
        elif lst[2] == lst[4] == lst[6]:
            self.win_lst.extend([2,4,6])
            print(self.win_lst)
            return True               

    def reset(self):
        for button in self.button_list:
            button.setText("")
            button.setEnabled(True)

        self.lst = list(range(9))
        self.random_list = list(range(9))
        self.label.setText("X's turn")

        # Clearing and reseting
        if self.win_lst:
            for i in range(3):
                eval(f"self.button{str(self.win_lst[i]+1)}").setStyleSheet("QPushButton {color: #ff4747;}")
        
        self.counter = 0
        self.win_lst = []
        self.flag = True
    

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()