from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
import constants as c
import game
import options


class Menu(QMainWindow):
    
    def start_loc_multi(self):
        """ Startet des lokalen Mehrspieler Modus
        """
        self.hide()
        g = game.Game(self, 'lok_multi')
        g.show()

    def start_ai(self):
        """ Startet den Computergegner Modus
        """
        self.hide()
        g = game.Game(self, 'ai_mode')
        g.show()

    def start_snake(self):
        """ Startet den Snake Modus
        """
        self.hide()
        g = game.Game(self, 'snake_mode')
        g.show()

    def start_bonus(self):
        print('Bonus Mode')


    def start_options(self):
        """ Öffnet die Einstellungen
        """
        self.hide()
        o = options.Options(self)
        o.show()

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

    def add_options(self):
        """ Fügt einen Butten hinzu um die Einstellungen zu öffnen
        """
        button = QPushButton('', self)
        button.move(10, 10)
        button.resize(60, 60)
        button.setIcon(QIcon('opt.png'))
        button.setIconSize(QSize(55, 55))
        button.clicked.connect(self.start_options)

    def add_text(self):
        """ Fügt den Titel TRON ein
        """
        text = QLabel('TRON', self)
        text.resize(c.MENU_WINDOW_WIDTH, 300)
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
        self.resize(c.MENU_WINDOW_WIDTH, c.MENU_WINDOW_HEIGHT)
        self.add_text()
        self.add_button(280, 'Local Multiplayer', self.start_loc_multi)
        self.add_button(340, 'V.S. AI', self.start_ai)
        self.add_button(400, 'Snake Mode', self.start_snake)
        self.add_button(460, 'Bonus Mode', self.start_bonus)
        self.add_options()
