from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import Car
import Expections


class Board(QFrame):
    boardWidth = 90
    boardHeigth = 60
    speed = 70
    isRunning = False
    isPaused = False


    def __init__(self):
        super().__init__()

        self.timer = QBasicTimer()

    def start(self):
        self.c1 = Car.Car(45, 30, 'E', 1)
        self.c1.addTail(15)
        self.isRunning = True
        self.timer.start(self.speed, self)

    def end(self):
        self.isRunning = False
        self.timer.stop()
        print("End")

    def pause(self):
        self.isPaused = True
        self.timer.stop()

    def endPause(self):
        self.isPaused = False
        self.timer.start(self.speed, self)

    def drawSquare(self, e, painter, x, y, c):
        '''draws a square of a shape'''        
        
        colorTable = [0x000000, 0x00A7B5, 0x00DEF0]  # noch nicht vollständig !!!

        color = QColor(colorTable[c])
        painter.fillRect(x*10, y*10, 10, 10, color)

    def paintEvent(self, e):
        painter = QPainter(self)

        #color = QColor(0x000000)
        #painter.fillRect(0, 0, 900, 600, color)

        tArr = self.c1.getTail()
        for i in tArr:
            self.drawSquare(e, painter, i.x, i.y, i.color)

        self.drawSquare(e, painter, self.c1.x, self.c1.y, self.c1.color)
        painter.end()

    def timerEvent(self, e):
        try:
            self.c1.move(1)
        except Expections.OutOfMapError:
            self.end()
        self.update()



class Game1(QMainWindow):    

        
    def keyPressEvent(self, e):
        if self.board.isPaused == True:         # Wenn das Spiel Pausiert ist, kann jede Taste das Spiel vortsetzen
            self.board.endPause()
        elif e.key() == Qt.Key_W:               # W -> Auto1 bewegt sich nach oben
            self.board.c1.changeDirection('N')
        elif e.key() == Qt.Key_A:               # A -> Auto1 bewegt sich nach links
            self.board.c1.changeDirection('W')
        elif e.key() == Qt.Key_S:               # S -> Auto1 bewegt sich nach unten
            self.board.c1.changeDirection('S')
        elif e.key() == Qt.Key_D:               # D -> Auto1 bewegt sich nach rechts
            self.board.c1.changeDirection('E')
        elif e.key() == Qt.Key_Space:           # Space -> Spiel wird (neu) gestartet
            if self.board.isRunning == False:
                self.board.start()
        elif e.key() == Qt.Key_Escape:          # Esc -> Spiel wird pausiert
            if self.board.isRunning == True:
                self.board.pause()
    
    
    def __init__(self, *args, **kwargs):
        super(Game1, self).__init__(*args, **kwargs)

        self.board = Board()
        self.setCentralWidget(self.board)

        self.board.start()

        self.setWindowTitle("Tron")
        self.resize(900, 600)

        self.show()
