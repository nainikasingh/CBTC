import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox

class RockPaperScissors(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Rock Paper Scissors Game')

        self.user_label = QLabel('Enter Rock/Paper/Scissors:', self)
        self.user_input = QLineEdit(self)
        self.result_label = QLabel('', self)

        self.btn_play = QPushButton('Play', self)
        self.btn_exit = QPushButton('Exit', self)

        self.btn_play.clicked.connect(self.play_game)
        self.btn_exit.clicked.connect(self.close)
        vbox = QVBoxLayout()
        vbox.addWidget(self.user_label)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.result_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_play)
        hbox.addWidget(self.btn_exit)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def play_game(self):
        user_pick = self.user_input.text().strip().capitalize()
        if user_pick not in ['Rock', 'Paper', 'Scissors']:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter Rock, Paper, or Scissors.')
            return

        comp_pick = random.choice(["Rock", "Paper", "Scissors"])

        result_msg = f'User Picked: {user_pick}\nComputer Picked: {comp_pick}\n'

        if user_pick == 'Rock':
            if comp_pick == 'Rock':
                result_msg += 'Result: Tie'
            elif comp_pick == 'Paper':
                result_msg += 'Result: Paper Wins'
            elif comp_pick == 'Scissors':
                result_msg += 'Result: Rock Wins'
        elif user_pick == 'Paper':
            if comp_pick == 'Rock':
                result_msg += 'Result: Paper Wins'
            elif comp_pick == 'Paper':
                result_msg += 'Result: Tie'
            elif comp_pick == 'Scissors':
                result_msg += 'Result: Scissors Wins'
        elif user_pick == 'Scissors':
            if comp_pick == 'Rock':
                result_msg += 'Result: Rock Wins'
            elif comp_pick == 'Paper':
                result_msg += 'Result: Scissors Wins'
            elif comp_pick == 'Scissors':
                result_msg += 'Result: Tie'

        self.result_label.setText(result_msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_window = RockPaperScissors()
    game_window.show()
    sys.exit(app.exec_())
