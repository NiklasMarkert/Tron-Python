from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
import constants as c

class HighscoreWindow(QMainWindow):

    def back_menu(self):
        self.close()
        self.parent().show()

    def add_back(self):
        button = QPushButton('< Back to Menu', self)
        button.move(10, 10)
        button.resize(120, 40)
        button.clicked.connect(self.back_menu)

    def add_titel(self):
        titel = QLabel('Highscore', self)
        titel.resize(c.HIGHSCORE_WINDOW_WIDTH, 80)
        font = titel.font()
        font.setBold(True)
        font.setPointSize(40)
        titel.setFont(font)
        titel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        titel.move(0, 0)

    def add_rank(self,pos, rank, color):
        rank = QLabel(str(rank) + '.', self)
        rank.resize(50, 50)
        font = rank.font()
        font.setBold(True)
        font.setPointSize(20)
        rank.setFont(font)
        rank.setAlignment(Qt.AlignVCenter)
        rank.move(200, 100)


    def __init__(self, parent, highscore):
        super(HighscoreWindow, self).__init__(parent)
        self.setWindowTitle('Tron')
        self.setFixedSize(c.HIGHSCORE_WINDOW_WIDTH, c.HIGHSCORE_WINDOW_HEIGHT)
        self.highscore = highscore
        self.add_titel()
        self.add_back()
        self.add_rank(0, 1, c.GOLD)
