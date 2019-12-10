from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt
import constants as c
import game


class Menu(QMainWindow):
    
    def start_game1(self):
        """ Startet des lokalen Mehrspieler Modus
        """
        self.hide()
        g = game.Game1(self, 'lok_multi')
        g.show()

    def start_game2(self):
        """ Startet den Computergegner Modus
        """
        print('V.S. KI')

    def start_game3(self):
        """ Startet den Snake Modus
        """
        self.hide()
        g = game.Game1(self, 'snake_mode')
        g.show()

    def start_game4(self):
        print('tbA')

    def add_button(self, pos, text, fkt):
        """ Fügt einen Butten hinzu um einen Spielmodus zu starten
        Eingabe: pos = Position des Buttons (durch y-Koordinate); text = Text der auf dem Button steht;
        fkt = Fuktion die ausgeführt wird, wenn der Button gedrückt wird
        """
        button = QPushButton(text, self)
        button.move(200, pos)
        button.resize(500, 50)
        button.setStyleSheet('QPushButton {font: bold; font-size: 30px}')
        button.clicked.connect(fkt)

    def add_text(self):
        """ Fügt den Titel TRON ein
        """
        text = QLabel('TRON', self)
        text.resize(c.WINDOW_WIDTH, 300)
        font = text.font()
        font.setBold(True)
        font.setPointSize(90)
        text.setFont(font)
        text.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        text.move(0, 0)
    
    def __init__(self):
        """ Konstruktor für das Menue
        """
        super(Menu, self).__init__()
        self.setWindowTitle('Tron')
        self.resize(c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
        self.add_button(280, 'Local Multiplayer', self.start_game1)
        self.add_button(340, 'V.S. KI', self.start_game2)
        self.add_button(400, 'Snake Mode', self.start_game3)
        self.add_button(460, 'tbA', self.start_game4)
        self.add_text()
