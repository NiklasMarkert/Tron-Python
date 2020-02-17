from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
#import constants as c
from constants import Modes as m, WindowSize as w, Options as o, Colors as c
import game
from highscore import highscore, highscore_window


class Menu(QMainWindow):

    def change_name(self, name):
        """ Ändert den Namen von Player1,
        nach Prüfung ob der Name zulässig ist
        """
        new_name = ''
        letter = False
        for i in name:
            if i != '%':
                new_name = new_name + i
                if i != ' ':
                    letter = True
        if new_name == '' or not letter:
            o.PLAYER_NAME = 'Unknown'
        else:
            o.PLAYER_NAME = new_name
   
    def start_game(self, mode):
        """ Startet den angegebenen Modus
        """
        self.hide()
        g = game.Game(self, mode, self.highscore)
        self.change_name(self.textbox.text())
        g.show()

    def show_highscores(self):
        """ Öffnet die Highscoreanzeige
        """
        self.hide()
        hsw = highscore_window.HighscoreWindow(self, self.highscore)
        hsw.show()

    def set_bots(self, amount):
        """ Setzt die Anzahl an Bots für den AI-Mode
        """
        for i in self.buttons1:
            i.setStyleSheet('QPushButton {font-size: 18px}')
        self.buttons1[amount-1].setStyleSheet('QPushButton {font: bold; font-size: 18px; background-color: ' + c.GREY + '}')
        o.AMOUNT_BOTS = amount

    def set_multiplayer(self, multi):
        """ Setzt ob im PowerUp-Mode gegen einen Computergegner oder
        einen lokalen Gegenspieler gespielt wird
        """
        for i in self.buttons2:
            i.setStyleSheet('QPushButton {font-size: 18px}')
        self.buttons2[multi].setStyleSheet('QPushButton {font: bold; font-size: 18px; background-color: ' + c.GREY + '}')
        o.MULTIPLAYER_PU = (multi == 1)

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

    def add_title(self):
        """ Fügt den Titel TRON ein
        """
        text = QLabel('TRON', self)
        text.resize(w.MENU_WINDOW_WIDTH, 300)
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
        text.resize(190, 30)
        font = text.font()
        font.setBold(True)
        font.setPointSize(14)
        text.setFont(font)
        text.move(10, 10)
        text.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 42)
        self.textbox.resize(190, 30)
        font = self.textbox.font()
        font.setPointSize(11)
        self.textbox.setFont(font)
        self.textbox.setText('Player1')

    def add_small_button(self, x, y, size, text, fkt):
        """ Fügt die Buttons für Anzahl Bots und Multiplayer im PowerUp-Mode ein
        """
        button = QPushButton(text, self)
        button.move(x, y)
        button.resize(size, 30)
        button.clicked.connect(fkt)
        return button

    def add_text(self, x, y, text):
        """ Fügt den Text über den kleinen Buttons ein
        """
        text = QLabel(text, self)
        text.resize(100, 30)
        font = text.font()
        font.setPointSize(10)
        text.setFont(font)
        text.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        text.move(x, y)

    def add_background(self):
        """ Setzt den weißen Hintergrund
        """
        bg = QLabel('', self)
        bg.resize(w.MENU_WINDOW_WIDTH, w.MENU_WINDOW_HEIGHT)
        bg.move(0,0)
        bg.setStyleSheet('QLabel {background-color : white;}')

    def __init__(self):
        """ Konstruktor für das Menü
        """
        super(Menu, self).__init__()
        self.setWindowTitle('Tron')
        self.setFixedSize(w.MENU_WINDOW_WIDTH, w.MENU_WINDOW_HEIGHT)
        self.add_background()        
        self.add_title()
        self.add_button(260, 'Local Multiplayer', lambda: self.start_game(m.MULTIPLAYER))
        self.add_button(320, 'V.S. AI', lambda: self.start_game(m.AI))
        self.add_button(380, 'Snake Mode', lambda: self.start_game(m.SNAKE))
        self.add_button(440, 'PowerUp Mode', lambda: self.start_game(m.POWER_UP))
        self.add_button(500, 'Highscores', self.show_highscores)
        self.add_textbox()
        self.buttons1 = [None, None, None]
        self.buttons1[0] = self.add_small_button(80, 330, 30, '1', lambda: self.set_bots(1))
        self.buttons1[1] = self.add_small_button(115, 330, 30, '2', lambda: self.set_bots(2))
        self.buttons1[2] = self.add_small_button(150, 330, 30, '3', lambda: self.set_bots(3))
        self.add_text(80, 300, 'Amount Bots')
        self.buttons2 = [None, None]
        self.buttons2[1] = self.add_small_button(80, 450, 47.5, 'Yes', lambda: self.set_multiplayer(1))
        self.buttons2[0] = self.add_small_button(132.5, 450, 47.5, 'No', lambda: self.set_multiplayer(0))
        self.add_text(80, 420, 'Multiplayer')
        self.set_bots(1)
        self.set_multiplayer(0)
        self.highscore = highscore.Highscore()
