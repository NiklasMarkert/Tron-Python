from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QColor
from constants import BoardSize as b
import expections
from player import car, ai
from highscore import scoreobject


class Board(QFrame):
    speed = 30
    is_running = False
    is_paused = False
    
    def print_out(self, output, text):
        output.setText(text)

    def set_out(self, big_out, small_out, score_display):
        self.big_out = big_out
        self.small_out = small_out
        self.score_display = score_display

    def clear_highscores(self):
        self.hst.setText('')
        self.hs1.setText('')
        self.hs2.setText('')
        self.hs3.setText('')

    def print_highscore(self, hs):
        """ Gibt die besten drei Scores am Ende eines Snakespiels aus
        """
        self.hst.setText('Highscores:')
        top3 = hs.get_scores(3)
        if len(top3) < 3:
            for i in range(len(top3), 3):
                top3 = top3 + [scoreobject.Scoreobject('---', '---', None)]
        self.hs1.setText('1. ' + top3[0].name + ' - ' + str(top3[0].score))
        self.hs2.setText('2. ' + top3[1].name + ' - ' + str(top3[1].score))
        self.hs3.setText('3. ' + top3[2].name + ' - ' + str(top3[2].score))

    def set_highscore(self, hst, hs1, hs2, hs3):
        self.hst = hst
        self.hs1 = hs1
        self.hs2 = hs2
        self.hs3 = hs3

    def set_background(self, background):
        self.background = background

    def __init__(self):
        super().__init__()
        self.timer = QBasicTimer()

    def run(self):
        self.is_running = True
        self.timer.start(self.speed, self)
        self.print_out(self.big_out, '')
        self.print_out(self.small_out, '')
        self.clear_highscores()
        self.background.hide()

    def end(self):
        self.is_running = False
        self.timer.stop()
        self.background.show()
        self.score_display.setText('')
        self.print_out(self.small_out, 'Press -Space- to restart or -M- to go to the menu')

    def pause(self):
        self.is_paused = True
        self.timer.stop()
        self.background.show()
        self.print_out(self.small_out, 'Press -M- to go to the menu or any other key to continue')
        self.print_out(self.big_out, '-- Pause --')

    def end_pause(self):
        self.is_paused = False
        self.timer.start(self.speed, self)
        self.background.hide()
        self.print_out(self.big_out, '')
        self.print_out(self.small_out, '')

    def draw_square(self, painter, x, y, color):        
        color = QColor(color)
        painter.fillRect(x * b.FIELD_SIZE, y * b.FIELD_SIZE, b.FIELD_SIZE, b.FIELD_SIZE, color)

    def draw_tail(self,painter, car):
        """ Zeichnet den Tail eines übergebenen Autos (car)
        """
        tail_arr = car.get_tail()
        for i in tail_arr:
            self.draw_square(painter, i.x, i.y, i.color)

    def draw_cars(self, painter, car_list):
        """ Zeichent alle Autos mit Schweif aus der car_list
        """
        for i in car_list:
            self.draw_tail(painter, i)
        for i in car_list:
            self.draw_square(painter, i.x, i.y, i.color)

    def draw_object(self, painter, x, y, color):
        """ Zeichnet ein einsammelbares Objekt/PowerUp
        """
        color = QColor(color)
        painter.fillRect(x * b.FIELD_SIZE - b.FIELD_SIZE/2, y * b.FIELD_SIZE - b.FIELD_SIZE/2, 2 *  b.FIELD_SIZE, 2 * b.FIELD_SIZE, color)

    def new_car(self, x, y, dir, color, name, tail_length):
        """ Erzeugt ein neues Auto und fügt es zur car_list hinzu
        """
        new_c = car.Car(x, y, dir, color, name)
        new_c.add_tail(tail_length)
        self.car_list = self.car_list + [new_c]
        return new_c

    def new_ai(self, x, y, dir, color, name, tail_length):
        """ Erzeugt eine neue KI und fügt diese zur car_list hinzu
        """
        new_ai = ai.AI(x, y, dir, color, name)
        new_ai.add_tail(tail_length)
        self.car_list = self.car_list + [new_ai]
        return new_ai

    def cars_move(self, car_list):
        for i in car_list:
            i.change_direction()
            self.move(i)
