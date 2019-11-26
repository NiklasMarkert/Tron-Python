from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import game


class Menu(QMainWindow):
    def start_game1(self):
        self.hide()
        g = game.Game1(self)
        g.show()

    def start_game2(self):
        print('Snake')

    def add_button(self, pos, text, fkt):
        button = QPushButton(text, self)
        button.move(200, pos)
        button.resize(500, 50)
        button.setStyleSheet('QPushButton {font: bold; font-size: 30px}')
        button.clicked.connect(fkt)

    def add_text(self):
        text = QLabel('TRON', self)
        text.resize(500, 300)
        font = text.font()
        font.setBold(True)
        font.setPointSize(90)
        text.setFont(font)
        text.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        text.move(200, 0)
    
    def __init__(self):
        super(Menu, self).__init__()
        self.setWindowTitle('Tron')
        self.resize(900, 600)
        self.add_button(280, 'Local Multiplayer', self.start_game1)
        self.add_button(340, 'Snake Mode', self.start_game2)
        self.add_text()
