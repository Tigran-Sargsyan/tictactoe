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
        self.setWindowTitle("TicTacToe")

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

    def mode(self, game_mode):
        """Selects the mode the user wants to play in
        Args:
            game_mode (int): 1-two_player mode, 2-VS computer mode
        Returns:
            None
        """

        self.game_mode = game_mode
        print('Game Mode: ', self.game_mode)
        self.mode1.deleteLater()
        self.mode2.deleteLater()

        if game_mode == 2: 
            self.square_list = list(range(9)) # For logic when playing with computer
    
    def click(self, btn, pos):
        """Manages the game process
        Args:
            btn (QPushButton): Button for clicking and playing
            pos (int): The assigned number of every button for controlling it
        Returns:
            None
        """

        if self.game_mode == 1:
            self.two_player(btn,pos) 
        elif self.game_mode == 2:
            self.vsCmp(btn,pos)    

    def two_player(self, btn, pos):
        """Manages the game process when playing in two_player and a button on the board is clicked
        Args:
            btn (QPushButton): Button for clicking and playing
            pos (int): The assigned number of every button for controlling it
        Returns:
            None
        """

        if self.move_counter % 2 == 0:
            btn.setText("X")
            btn.setEnabled(False)
            self.label.setText("O's turn!")
            self.board[pos]="X"
            self.win(self.board,"X")

        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.label.setText("X's turn")
            self.board[pos]="O"
            self.win(self.board,"O")
    
        print(self.board)
        self.move_counter += 1  # incrementing the counter after each move

    def vsCmp(self, btn, pos):
        """Manages the game process when playing in vs Computer mode and a button on the board is clicked
        Args:
            btn (QPushButton): Button for clicking and playing
            pos (int): The assigned number of every button for controlling it
        Returns:
            None
        """
        
        btn.setText("X")
        btn.setEnabled(False)
        self.label.setText("X's turn!")
        self.board[pos]="X"
        self.square_list.remove(pos)
        self.win(self.board,"X")
        print(self.board)

        if self.flag:
            print('move_counter = ', self.move_counter)
            print(self.square_list,"random list before picking")

            if self.move_counter == 4:
                self.flag == False
                return

            pick = self.move_decision(pos)
            self.square_list.remove(pick)
            print(self.square_list,"random list after picking")
            eval(f"self.btn{pick+1}").setText("O") 
            eval(f"self.btn{pick+1}").setEnabled(False)
            self.board[pick] = "O"
            self.win(self.board,"O")    
            self.move_counter += 1  

    def move_decision(self, pos):
        """Decides the next move playing optimal strategy
        Args:
            pos (int): The last position where the players put an X
        Returns:
            pick (int): The square that the algorithm picked as current best move
        """

        board = np.array(self.board).reshape(3,3)
        print(board)
        if self.move_counter == 0:
            if (pos == 0 or pos == 2 or pos == 6 or pos == 8) and self.move_counter == 0:
                pick = self.square_list[4]
            elif pos == 4 and self.move_counter == 0:
                pick = random.choice(self.square_list[0:3:2] + self.square_list[5:8:2])      
            else:
                pick = random.choice(self.square_list)   

        else:
            threat_square = self.find_threat_square(board)
            if threat_square:
                pick = int(threat_square)
                print('picked square: ', pick)
                # TODO
            else: #self.square_list:
                pick = random.choice(self.square_list) 

        return pick

    def find_threat_square(self,board):
        """A function that finds if there are any row, column or diagonal threats
        Args:
            board (ndarray): A 3x3 ndarray representing the board
        Returns:
            row_threat_square (int): The square where there is a row threat
            col_threat_square (int): The square where there is a column threat
            diag1_threat_square (int): The square where there is a diagonal threat
            diag2_threat_square (int): The square where there is a diagonal threat
        """

        for i in range(3):
            row = board[i]
            col = board[:,i] 
            row_threat_square = self.check_line_threat(row)
            col_threat_square = self.check_line_threat(col)
            if row_threat_square:
                return row_threat_square
            elif col_threat_square:
                return col_threat_square

        diag1_threat_square = self.check_line_threat(np.diag(board))
        if diag1_threat_square:
            return diag1_threat_square

        diag2_threat_square = self.check_line_threat(np.diag(np.fliplr(board)))
        if diag2_threat_square:
            return diag2_threat_square

        return False

    def check_line_threat(self, line):
        """A function to check the row, column and diagonal threats
        
        Args:
            line (ndarray): row, column or diagonal
        Returns:
            line[j] (int): threat square
            False (bool): A boolean value if there is no threat 
        """

        if np.sum(line == 'X') == 2 and np.sum(line == 'O') == 0:
            for j in range(3):
                if line[j] != 'X':
                    return line[j]
        return False

    def win(self, board, player):
        """Checks if the winning condition occured
        Args:
            board (ndarray): The 3x3 game board
            player (str): "X" or "O"
        Returns:
            None (Changes the global flag for controlling the game process)
        """

        if self.check_horizontal(board) or self.check_vertical(board) or self.check_diagonal(board):
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

    def check_horizontal(self, board):
        """Helper of win() that checks horizontals
        
        Args:
            board (ndarray): The 3x3 game board
        Returns:
            True (bool): If the winning condition on the diagonal was achieved
        """
        for i in range(3):
            if board[i] == board[i+3] == board[i+6]:
                self.win_lst.extend([i,i+3,i+6])
                print(self.win_lst)
                return True

    def check_vertical(self, board):
        """Helper of win() that checks horizontals
        
        Args:
            board (ndarray): The 3x3 game board
        
        Returns:
            True (bool): If the winning condition on the vertical was achieved
        """

        for i in range(0,7,3):
            if board[i] == board[i+1] == board[i+2]:
                self.win_lst.extend([i,i+1,i+2])
                print(self.win_lst)
                return True

    def check_diagonal(self, lst):
        """Helper of win() that checks horizontals
        
        Args:
            board (ndarray): The 3x3 game board
        Returns:
            True (bool): If the winning condition on the diagonal was achieved
        """

        if lst[0] == lst[4] == lst[8]:
            self.win_lst.extend([0,4,8])
            print(self.win_lst)
            return True

        elif lst[2] == lst[4] == lst[6]:
            self.win_lst.extend([2,4,6])
            print(self.win_lst)
            return True    

    def reset(self):
        """Resets all the elements in the game window
        Args:
            None
        Returns:
            None
        """

        for button in self.button_list:
            button.setText("")
            button.setEnabled(True)

        self.board = list(range(9))
        self.square_list = list(range(9))
        self.label.setText("X's turn")

        # Clearing and reseting
        if self.win_lst:
            for i in range(3):
                eval(f"self.btn{str(self.win_lst[i]+1)}").setStyleSheet("QPushButton {color: #ff4747;}")
        
        self.move_counter = 0
        self.win_lst = []
        self.flag = True


def main():
    app = QApplication(sys.argv)
    game_window = Window()
    game_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
