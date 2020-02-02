from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
import constants as c
import game
import options
import highscore
import highscore_window


class Menu(QMainWindow):

    def change_name(self, name):
        new_name = ''
        for i in name:
            if i != '%':
                new_name = new_name + i
        if new_name == '':
            c.PLAYER_NAME = 'Unknown'
        else:
            c.PLAYER_NAME = new_name
    
    def start_loc_multi(self):
        """ Startet des lokalen Mehrspieler Modus
        """
        self.hide()
        g = game.Game(self, 'lok_multi', self.highscore)
        self.change_name(self.textbox.text())
        g.show()

    def start_ai(self):
        """ Startet den Computergegner Modus
        """
        self.hide()
        g = game.Game(self, 'ai_mode', self.highscore)
        self.change_name(self.textbox.text())
        g.show()

    def start_snake(self):
        """ Startet den Snake Modus
        """
        self.hide()
        g = game.Game(self, 'snake_mode', self.highscore)
        self.change_name(self.textbox.text())
        g.show()

    def start_powerup(self):
        """ Startet den PowerUp Modus
        """
        print('PowerUp Mode')

    def start_options(self):
        """ Öffnet die Einstellungen
        """
        self.hide()
        o = options.Options(self)
        o.show()

    def show_highscores(self):
        """ Öffnet die Highscoreanzeige
        """
        self.hide()
        hsw = highscore_window.HighscoreWindow(self, self.highscore)
        hsw.show()
        self.highscore.print_out()

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
    
    def add_textbox(self):
        """ Fügt eine Textbox hinzu, um den Spielernamen einzugeben
        """
        text = QLabel('Player Name:', self)
        text.resize(150, 20)
        font = text.font()
        font.setBold(True)
        font.setPointSize(10)
        text.setFont(font)
        text.move(c.MENU_WINDOW_WIDTH - 160, 10)
        self.textbox = QLineEdit(self)
        self.textbox.move(c.MENU_WINDOW_WIDTH - 160, 30)
        self.textbox.resize(150, 25)
        self.textbox.setText('Player1')

    def __init__(self):
        """ Konstruktor für das Menü
        """
        super(Menu, self).__init__()
        self.setWindowTitle('Tron')
        self.setFixedSize(c.MENU_WINDOW_WIDTH, c.MENU_WINDOW_HEIGHT)
        self.add_text()
        self.add_button(260, 'Local Multiplayer', self.start_loc_multi)
        self.add_button(320, 'V.S. AI', self.start_ai)
        self.add_button(380, 'Snake Mode', self.start_snake)
        self.add_button(440, 'PowerUp Mode', self.start_powerup)
        self.add_button(500, 'Highscores', self.show_highscores)
        self.add_textbox()
        self.add_options()
        self.highscore = highscore.Highscore()
