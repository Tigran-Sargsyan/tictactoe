import sys
import random
import time
import numpy as np

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QIcon


class ChooseGameMode(QWidget):
    def __init__(self):
        super().__init__()

        self.window_width = 502
        self.window_height = 570

        # Geometry of the window
        self.setGeometry(500, 100, 462, 570)
        self.setMinimumSize(self.window_width, self.window_height)
        self.setMaximumSize(self.window_width, self.window_height)

        # Styling of the window
        self.setWindowTitle("TicTacToe")
        self.setWindowIcon(QIcon("icon.jpg"))
        self.setStyleSheet('background-color: #adc9c3;')

        # A label to display the message
        welcome = QtWidgets.QLabel('Welcome to TicTacToe!', self)
        welcome.setGeometry(40, 10, 400, 70)
        welcome.setStyleSheet("QLabel{font-size: 20pt;color: green;}")

        # A label to choose the game mode
        label = QtWidgets.QLabel('Choose the game mode', self)
        label.setGeometry(45, 70, 400, 140)
        label.setStyleSheet("QLabel{font-size: 18pt;}")

        # Buttons for the game modes
        self.two_players_button = QtWidgets.QPushButton('2 Players', self, width=200, height=150)
        self.two_players_button.clicked.connect(self.two_players_selected)
        self.two_players_button.move(165, 200)
        self.two_players_button.setStyleSheet("QPushButton{font-size: 19pt;}")

        self.vs_computer_button = QtWidgets.QPushButton('VS Computer', self, width=200, height=150)
        self.vs_computer_button.clicked.connect(self.vs_computer_selected)
        self.vs_computer_button.move(130, 300)
        self.vs_computer_button.setStyleSheet("QPushButton{font-size: 19pt;}")

    def two_players_selected(self):
        # Window.mode(Window, 1)
        Window.game_mode = '2 player'
        self.close()

    def vs_computer_selected(self):
        # Window.mode(Window, 2)
        Window.game_mode = 'vs computer'
        self.close()


class Window(QMainWindow):
    """
    A class of the game Window inheriting from QMainWindow class
    that gives us the GUI interface
    """

    def __init__(self):
        super(Window, self).__init__()

        self.window_width = 502
        self.window_height = 570
        # Geometry of the window
        self.setGeometry(500, 100, 462, 570)
        self.setMinimumSize(self.window_width, self.window_height)
        self.setMaximumSize(self.window_width, self.window_height)

        self.setWindowTitle("TicTacToe")
        self.setWindowIcon(QIcon("icon.jpg"))

        self.move_counter = 0  # A counter to determine whose move it is
        self.flag = True  # A flag to tell if a game is still in process
        # self.game_mode = 0  # A variable for holding the mode of the game (1: 2Player, 2:vs Computer)

        self.board = list(range(9))  # Defining a list with values [0,8] for storing X-s and O-s

        self.win_lst = []  # Defining a list to hold the winning squares

        # Counting how many times has each player won for showing it in the interface
        self.winX = 0
        self.winY = 0

        self.initUI()  # A function for the UI of the window

    def initUI(self):
        """Creating buttons,setting geometry,text in the buttons,styling"""

        self.btn1 = QtWidgets.QPushButton(self)  # btn1 to btn9 are the squares of the playing board
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn3 = QtWidgets.QPushButton(self)
        self.btn4 = QtWidgets.QPushButton(self)
        self.btn5 = QtWidgets.QPushButton(self)
        self.btn6 = QtWidgets.QPushButton(self)
        self.btn7 = QtWidgets.QPushButton(self)
        self.btn8 = QtWidgets.QPushButton(self)
        self.btn9 = QtWidgets.QPushButton(self)

        self.btn10 = QtWidgets.QPushButton(self)  # btn10 is clicked when the user wants to play again
        self.btn10.setText("Play again")
        self.btn10.setFont(QFont('Times', 28))

        # Initializing x coordinates
        x1 = 25
        x2 = x1 + 151
        x3 = x2 + 151

        # Initializng y coordinates
        y1 = 10
        y2 = 10 + 101
        y3 = y2 + 101

        # Initializing width and height
        width = 150
        height = 100

        self.btn1.setGeometry(x1, y1, width, height)
        self.btn2.setGeometry(x2, y1, width, height)
        self.btn3.setGeometry(x3, y1, width, height)
        self.btn4.setGeometry(x1, y2, width, height)
        self.btn5.setGeometry(x2, y2, width, height)
        self.btn6.setGeometry(x3, y2, width, height)
        self.btn7.setGeometry(x1, y3, width, height)
        self.btn8.setGeometry(x2, y3, width, height)
        self.btn9.setGeometry(x3, y3, width, height)

        self.btn10.setGeometry(0, 430, self.window_width + 5, 70)

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
        self.label.setGeometry(290, 350, 200, 60)
        self.label.setText("X's turn!")
        self.label.setStyleSheet("QLabel{font-size: 27pt;}")

        self.player1 = QtWidgets.QLabel(self)  # Label to show the player1
        self.player2 = QtWidgets.QLabel(self)  # Label to show the player2

        self.player1.setStyleSheet("QLabel{font-size: 18pt;}")
        self.player2.setStyleSheet("QLabel{font-size: 18pt;}")

        self.score_1 = QtWidgets.QLabel(self)  # Label to show the score of player1
        self.score_1.setText("0")
        self.score_1.setStyleSheet("QLabel{font-size: 18pt;}")

        self.score_2 = QtWidgets.QLabel(self)  # Label to show the score of player2
        self.score_2.setText("0")
        self.score_2.setStyleSheet("QLabel{font-size: 18pt;}")

        player_lbl_width = 130
        player_lbl_height = 55
        player_lbl_x = 10
        player1_lbl_y = 320
        player2_lbl_y = player1_lbl_y + 50

        if self.game_mode == '2 player':
            self.player1.setText("Player1: ")
            self.player1.setGeometry(player_lbl_x, player1_lbl_y, player_lbl_width, player_lbl_height)
            print(1)
            self.score_1.setGeometry(150, 329, 45, 40)
            print(2)
            self.player2.setText("Player2: ")
            self.player2.setGeometry(player_lbl_x, player2_lbl_y, player_lbl_width, player_lbl_height)
            self.score_2.setGeometry(150, 379, 45, 40)

        elif self.game_mode == 'vs computer':
            self.player1.setText("You:")
            self.player1.setGeometry(player_lbl_x, player1_lbl_y, player_lbl_width, player_lbl_height)
            self.score_1.setGeometry(200, 329, 75, 40)
            self.player2.setText("Computer:")
            self.player2.setGeometry(player_lbl_x, player2_lbl_y, player_lbl_width + 35, player_lbl_height)
            self.score_2.setGeometry(200, 379, 75, 40)
            self.square_list = list(range(9))  # For logic when playing with computer

        # Styling
        self.setStyleSheet('background-color: #adc9c3;')
        self.btn1.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn2.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn3.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn4.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn5.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn6.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn7.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn8.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn9.setStyleSheet("QPushButton {color: #ff0000;}")
        self.btn10.setStyleSheet("background-color: #4b7173")

        # Clicking the buttons
        self.btn1.clicked.connect(lambda: self.click(self.btn1, 0))
        self.btn2.clicked.connect(lambda: self.click(self.btn2, 1))
        self.btn3.clicked.connect(lambda: self.click(self.btn3, 2))
        self.btn4.clicked.connect(lambda: self.click(self.btn4, 3))
        self.btn5.clicked.connect(lambda: self.click(self.btn5, 4))
        self.btn6.clicked.connect(lambda: self.click(self.btn6, 5))
        self.btn7.clicked.connect(lambda: self.click(self.btn7, 6))
        self.btn8.clicked.connect(lambda: self.click(self.btn8, 7))
        self.btn9.clicked.connect(lambda: self.click(self.btn9, 8))
        self.btn10.clicked.connect(self.reset)

    def click(self, btn, pos):
        """Manages the game process

        Args:
            btn (QPushButton): Button for clicking and playing
            pos (int): The assigned number of every button for controlling it

        Returns:
            None

        """

        if self.game_mode == '2 player':
            self.two_player(btn, pos)
        elif self.game_mode == 'vs computer':
            self.vsCmp(btn, pos)

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
            self.board[pos] = "X"
            self.win(self.board, "X")

        else:
            btn.setText("O")
            btn.setEnabled(False)
            self.label.setText("X's turn!")
            self.board[pos] = "O"
            self.win(self.board, "O")

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
        time.sleep(0.15)
        btn.setEnabled(False)
        self.label.setText("X's turn!")
        self.board[pos] = "X"
        self.square_list.remove(pos)
        self.win(self.board, "X")
        print(self.board)

        if self.flag:
            print('move_counter = ', self.move_counter)
            print(self.square_list, "random list before picking")

            if self.move_counter == 4:
                self.flag = False
                return

            pick = self.move_decision(pos)
            self.square_list.remove(pick)
            print(self.square_list, "random list after picking")
            eval(f"self.btn{pick + 1}").setText("O")
            eval(f"self.btn{pick + 1}").setEnabled(False)
            self.board[pick] = "O"
            self.win(self.board, "O")
            self.move_counter += 1

    def move_decision(self, pos):
        """Decides the next move playing optimal strategy

        Args:
            pos (int): The last position where the players put an X

        Returns:
            pick (int): The square that the algorithm picked as current best move

        """

        board = np.array(self.board).reshape(3, 3)
        pick = 0
        print(board)
        if self.move_counter == 0:
            if (pos == 0 or pos == 2 or pos == 6 or pos == 8):
                pick = 4
            elif pos == 1:
                pick = random.choice([0, 2, 4, 7])
            elif pos == 3:
                pick = random.choice([0, 4, 5, 6])
            elif pos == 5:
                pick = random.choice([2, 3, 4, 8])
            elif pos == 7:
                pick = random.choice([1, 4, 6, 8])
            elif pos == 4:
                pick = random.choice(self.square_list[0:3:2] + self.square_list[5:8:2])

        else:
            win_square = self.check_win_move(board)
            if win_square:
                pick = int(win_square)
                return pick

            threat_square = self.find_threat_square(board)
            if threat_square:
                pick = int(threat_square)
                print('picked square: ', pick)
                # TODO
            else:  # self.square_list:
                pick = random.choice(self.square_list)

        print('pick: ', pick)
        return pick

    def check_win_move(self, board):
        """Checks if there is a winning move on each line

        Args:
            board (ndarray): A 3x3 ndarray representing the board

        Returns:
            row_win_square (str): A square in a row where you can put 'O' and win
            col_win_square (str): A square in a column where you can put 'O' and win
            diag_win_square (str): A square in a diagonal where you can put 'O' and win
            False (bool): If no winning move has been found

        """

        for i in range(3):
            row = board[i]
            col = board[:, i]
            row_win_square = self.check_line_win(row)
            if (row_win_square):
                return row_win_square
            col_win_square = self.check_line_win(col)
            if (col_win_square):
                return col_win_square

        diag_win_square = self.check_line_win(np.diag(board))
        if diag_win_square:
            return diag_win_square

        diag_win_square = self.check_line_win(np.diag(np.fliplr(board)))
        if diag_win_square:
            return diag_win_square

        return False

    def check_line_win(self, line):
        """Checks if there is a winning move in the given line

        Args:
            line (ndarray, 1D): A row, column or diagonal to check

        Returns:
            line[j] (str): The string number (location) in the board
            False (bool): If no winning move has been found

        """

        if np.sum(line == 'O') == 2 and np.sum(line == 'X') == 0:
            for j in range(3):
                if line[j] != 'O':
                    return line[j]

        return False

    def find_threat_square(self, board):
        """A function that finds if there are any row, column or diagonal threats

        Args:
            board (ndarray): A 3x3 ndarray representing the board

        Returns:
            row_threat_square (int): The square where there is a row threat
            col_threat_square (int): The square where there is a column threat
            diag_threat_square (int): The square where there is a diagonal threat
            False (bool): If no threat has been found

        """

        for i in range(3):
            row = board[i]
            col = board[:, i]
            row_threat_square = self.check_line_threat(row)
            if row_threat_square:
                return row_threat_square
            col_threat_square = self.check_line_threat(col)
            if col_threat_square:
                return col_threat_square

        diag_threat_square = self.check_line_threat(np.diag(board))
        if diag_threat_square:
            return diag_threat_square

        diag_threat_square = self.check_line_threat(np.diag(np.fliplr(board)))
        if diag_threat_square:
            return diag_threat_square

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
                eval(f"self.btn{str(self.win_lst[i] + 1)}").setStyleSheet("QPushButton {color: #0101e8;}")

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
            if board[i] == board[i + 3] == board[i + 6]:
                self.win_lst.extend([i, i + 3, i + 6])
                print(self.win_lst)
                return True

    def check_vertical(self, board):
        """Helper of win() that checks horizontals

        Args:
            board (ndarray): The 3x3 game board

        Returns:
            True (bool): If the winning condition on the vertical was achieved

        """

        for i in range(0, 7, 3):
            if board[i] == board[i + 1] == board[i + 2]:
                self.win_lst.extend([i, i + 1, i + 2])
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
            self.win_lst.extend([0, 4, 8])
            print(self.win_lst)
            return True

        elif lst[2] == lst[4] == lst[6]:
            self.win_lst.extend([2, 4, 6])
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
        self.label.setText("X's turn!")

        # Clearing and reseting
        if self.win_lst:
            for i in range(3):
                eval(f"self.btn{str(self.win_lst[i] + 1)}").setStyleSheet("QPushButton {color: #ff0000;}")

        self.move_counter = 0
        self.win_lst = []
        self.flag = True


def main():
    app_ = QApplication([])
    choose_game_mode = ChooseGameMode()
    choose_game_mode.show()
    app_.exec_()
    game()


def game():
    app = QApplication(sys.argv)
    game_window = Window()
    game_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
