from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtCore import Qt
import constants as c
from modes import snakemode, multiplayermode, aimode


class Game(QMainWindow):
    
    def close_game(self):
        self.close()
        self.parent().show()

    def arrow_keys(self, e):
        if e.key() == c.PLAYER2_UP:            # Pfeiltaste nach oben -> Auto2 bewegt sich nach oben
            self.board.c2.next_dir = c.NORTH
        elif e.key() == c.PLAYER2_LEFT:        # Pfeiltaste nach links -> Auto2 bewegt sich nach links
            self.board.c2.next_dir = c.WEST
        elif e.key() == c.PLAYER2_DOWN:        # Pfeiltaste nach unten -> Auto2 bewegt sich nach unten
            self.board.c2.next_dir = c.SOUTH
        elif e.key() == c.PLAYER2_RIGHT:       # Pfeiltaste nach rechts -> Auto2 bewegt sich nach rechts
            self.board.c2.next_dir = c.EAST

    def keyPressEvent(self, e):
        if self.board.is_paused:                # Wenn das Spiel Pausiert ist, kann jede Taste das Spiel vortsetzen
            if e.key() == c.MENU:             # Nur M beendet das Spiel und geht zurück zum Menü
                self.close_game()
            else:
                self.board.end_pause()
        elif e.key() == c.PLAYER1_UP:               # W -> Auto1 bewegt sich nach oben
            self.board.c1.next_dir = c.NORTH
        elif e.key() == c.PLAYER1_RIGHT:               # A -> Auto1 bewegt sich nach links
            self.board.c1.next_dir = c.EAST
        elif e.key() == c.PLAYER1_DOWN:               # S -> Auto1 bewegt sich nach unten
            self.board.c1.next_dir = c.SOUTH
        elif e.key() == c.PLAYER1_LEFT:               # D -> Auto1 bewegt sich nach rechts
            self.board.c1.next_dir = c.WEST
        elif self.multiplayer:
            self.arrow_keys(e)
        if self.board.is_running is False:      # Falls Spiel beendet:
            if e.key() == c.START:             # Leertaste -> Startet Spiel neu
                self.board.start()
                self.board.run()
            elif e.key() == c.MENU:               # M -> Kehre zum Menü zurück
                self.close_game()
        elif e.key() == c.PAUSE:          # Esc -> Spiel wird pausiert
            if self.board.is_running:
                self.board.pause()
     
    def add_output1(self):
        self.label1 = QLabel('', self)
        self.label1.resize(c.BOARD_WINDOW_WIDTH, 50)
        font = self.label1.font()
        font.setBold(True)
        font.setPointSize(30)
        self.label1.setFont(font)
        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label1.move(0, c.BOARD_WINDOW_HEIGHT - 100)

    def add_output2(self):
        self.label2 = QLabel('Press -Space- to start', self)
        self.label2.resize(c.BOARD_WINDOW_WIDTH, 50)
        font = self.label2.font()
        font.setBold(True)
        font.setPointSize(15)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label2.move(0, c.BOARD_WINDOW_HEIGHT - 50)

    def __init__(self, parent, mode):
        super(Game, self).__init__(parent)
        self.multiplayer = False
        if mode == 'lok_multi':
            self.board = multiplayermode.LokMulti()
            self.multiplayer = True
        elif mode == 'snake_mode':
            self.board = snakemode.SnakeMode()
        elif mode == 'ai_mode':
            self.board = aimode.AIMode()
        self.setCentralWidget(self.board)
        self.add_output1()
        self.add_output2()
        self.board.set_out(self.label1, self.label2)
        self.board.start()
        self.setWindowTitle('Tron')
        self.resize(c.BOARD_WINDOW_WIDTH, c.BOARD_WINDOW_HEIGHT)
 
