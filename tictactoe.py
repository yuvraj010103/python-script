import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QGridLayout, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Tic-Tac-Toe - PyQt5')
        self.setGeometry(100, 100, 320, 400)
        
        # 3x3 game board
        self.buttons = [[QPushButton('') for _ in range(3)] for _ in range(3)]
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = random.choice(['X', 'O'])
        
        grid_layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setFixedSize(90, 90)
                self.buttons[i][j].setFont(self.buttons[i][j].font().setPointSize(36))
                self.buttons[i][j].setStyleSheet("QPushButton { border: 2px solid gray; }")
                self.buttons[i][j].clicked.connect(lambda checked, row=i, col=j: self.play_turn(row, col))
                grid_layout.addWidget(self.buttons[i][j], i, j)
        
        self.status_label = QLabel(f"Player {self.current_player}'s Turn")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        
        reset_btn = QPushButton('New Game')
        reset_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; font-weight: bold; padding: 10px; }")
        reset_btn.clicked.connect(self.reset_game)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addLayout(grid_layout)
        main_layout.addWidget(reset_btn)
        
        self.setLayout(main_layout)
    
    def play_turn(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            
            if self.check_winner():
                self.status_label.setText(f"Player {self.current_player} WINS!")
                self.status_label.setStyleSheet("font-size: 18px; color: green; font-weight: bold; padding: 10px;")
            elif self.is_board_full():
                self.status_label.setText("Game Draw!")
                self.status_label.setStyleSheet("font-size: 18px; color: orange; font-weight: bold; padding: 10px;")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText(f"Player {self.current_player}'s Turn")
    
    def check_winner(self):
        # Rows, columns, diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False
    
    def is_board_full(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))
    
    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
        self.current_player = random.choice(['X', 'O'])
        self.status_label.setText(f"Player {self.current_player}'s Turn")
        self.status_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
