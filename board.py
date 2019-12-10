from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QColor
import constants as c
import expections

class Board(QFrame):
    speed = 40
    is_running = False
    is_paused = False
    
    def print_out(self, output, text):
        output.setText(text)

    def set_out(self, big_out, small_out):
        self.big_out = big_out
        self.small_out = small_out

    def __init__(self):
        super().__init__()
        self.timer = QBasicTimer()

    def run(self):
        self.is_running = True
        self.timer.start(self.speed, self)
        self.print_out(self.big_out, '')
        self.print_out(self.small_out, '')

    def end(self):
        self.is_running = False
        self.timer.stop()
        self.print_out(self.small_out, 'Press -Space- to restart or -M- to go to the menu')

    def pause(self):
        self.is_paused = True
        self.timer.stop()
        self.print_out(self.small_out, 'Press -M- to go to the menu or any other key to continue')
        self.print_out(self.big_out, '-- Pause --')

    def end_pause(self):
        self.is_paused = False
        self.timer.start(self.speed, self)
        self.print_out(self.big_out, '')
        self.print_out(self.small_out, '')

    def draw_square(self, painter, x, y, color):        
        color = QColor(color)
        painter.fillRect(x * c.FIELD_SIZE, y * c.FIELD_SIZE, c.FIELD_SIZE, c.FIELD_SIZE, color)

    def draw_tail(self, car, painter):
        tail_arr = car.get_tail()
        for i in tail_arr:
            self.draw_square(painter, i.x, i.y, i.color)