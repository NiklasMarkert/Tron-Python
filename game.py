from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import expections
import car


class Board(QFrame):
    speed = 40
    is_running = False
    is_paused = False

    def __init__(self):
        super().__init__()
        self.timer = QBasicTimer()

    def start(self):
        self.next_dir1 = 'N'
        self.c1 = car.Car(30, 30, 'N', 1, True, 'Player1')
        self.c1.add_tail(50)
        self.next_dir2 = 'S'
        self.c2 = car.Car(60, 30, 'S', 3, True, 'Player2')
        self.c2.add_tail(50)

    def run(self):
        self.is_running = True
        self.timer.start(self.speed, self)

    def end(self):
        self.is_running = False
        self.timer.stop()
        print('End -- Press <Space> to restart or <M> to go to the menu')

    def pause(self):
        self.is_paused = True
        self.timer.stop()
        print('Pause -- Press <M> to go to the menu or any other key to continue')

    def end_pause(self):
        self.is_paused = False
        self.timer.start(self.speed, self)

    def draw_square(self, painter, x, y, c):        
        color_table = [0x000000, 0x00A7B5, 0x00DEF0,
                       0xD500C1, 0xFE54EE]  # noch nicht vollständig !!!
        color = QColor(color_table[c])
        painter.fillRect(x*10, y*10, 10, 10, color)

    def draw_tail(self, car, painter):
        tail_arr = car.get_tail()
        for i in tail_arr:
            self.draw_square(painter, i.x, i.y, i.color)

    def paintEvent(self, e):
        painter = QPainter(self)
        self.draw_tail(self.c1, painter)
        self.draw_tail(self.c2, painter)
        self.draw_square(painter, self.c1.x, self.c1.y, self.c1.color)
        self.draw_square(painter, self.c2.x, self.c2.y, self.c2.color)
        painter.end()

    def test_collision(self, car, enemy):
        tail_arr = enemy.get_tail()
        for i in tail_arr:
            if car.x == i.x and car.y == i.y:
                raise expections.Collision
                break

    def move(self, car, enemy):
        try:
            car.move(1)
            self.test_collision(car, enemy)
        except (expections.OutOfMapError, expections.SelfDestruction, expections.Collision):
            print("\n" + car.name + " lost")
            self.end()

    def timerEvent(self, e):
        self.c1.change_direction(self.next_dir1)
        self.c2.change_direction(self.next_dir2)
        self.move(self.c1, self.c2)
        self.move(self.c2, self.c1)
        self.update()


class Game1(QMainWindow):    
    
    def close_game(self):
        self.close()
        self.parent().show()

    def keyPressEvent(self, e):
        if self.board.is_paused:                # Wenn das Spiel Pausiert ist, kann jede Taste das Spiel vortsetzen
            if e.key() == Qt.Key_M:             # Nur M beendet das Spiel und geht zurück zum Menü
                self.close_game()
            else:
                self.board.end_pause()
        elif e.key() == Qt.Key_W:               # W -> Auto1 bewegt sich nach oben
            self.board.next_dir1 = 'N'
        elif e.key() == Qt.Key_A:               # A -> Auto1 bewegt sich nach links
            self.board.next_dir1 = 'W'
        elif e.key() == Qt.Key_S:               # S -> Auto1 bewegt sich nach unten
            self.board.next_dir1 = 'S'
        elif e.key() == Qt.Key_D:               # D -> Auto1 bewegt sich nach rechts
            self.board.next_dir1 = 'E'
        elif e.key() == Qt.Key_Up:              # Pfeiltaste nach oben -> Auto2 bewegt sich nach oben
            self.board.next_dir2 = 'N'
        elif e.key() == Qt.Key_Left:            # Pfeiltaste nach links -> Auto2 bewegt sich nach links
            self.board.next_dir2 = 'W'
        elif e.key() == Qt.Key_Down:            # Pfeiltaste nach unten -> Auto2 bewegt sich nach unten
            self.board.next_dir2 = 'S'
        elif e.key() == Qt.Key_Right:           # Pfeiltaste nach rechts -> Auto2 bewegt sich nach rechts
            self.board.next_dir2 = 'E'
        elif self.board.is_running is False:    # Falls Spiel beendet:
            if e.key() == Qt.Key_Space:             # Leertaste -> Startet Spiel neu
                self.board.start()
                self.board.run()
            elif e.key() == Qt.Key_M:               # M -> Kehre zum Menü zurück
                self.close_game()
        elif e.key() == Qt.Key_Escape:          # Esc -> Spiel wird pausiert
            if self.board.is_running:
                self.board.pause()
       
    def __init__(self, parent):
        super(Game1, self).__init__(parent)
        
        self.board = Board()
        self.setCentralWidget(self.board)
        self.board.start()

        self.setWindowTitle('Tron')
        self.resize(900, 600)
        print('Press <Space> to start the game')
 
