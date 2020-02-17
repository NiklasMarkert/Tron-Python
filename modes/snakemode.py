from PyQt5.QtGui import QPainter, QColor
from constants import Directions as d, StartingPositions as s, Colors as c, Options as o
import expections
import board
import objects

class SnakeMode(board.Board):

    def __init__(self, hs):
        super().__init__()
        self.highscore = hs

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(s.START_X_1P, s.START_Y_1P, d.NORTH, c.BLUE, o.PLAYER_NAME, 20)
        self.obj_arr = [None]
        self.score = 0
        self.score_display.setStyleSheet('QLabel { color : black; }')
        self.update_score(0)

    def update_score(self, score):
        """ Es wird der Score der oben recht angezeigt wird aktuallisiert
        """
        top3 = self.highscore.get_scores(3)
        if (len(top3) >= 3 and score > top3[2].score) or len(top3) < 3: # Sollte der Aktuelle Score den allgemeinen 3. Platz bringen ist er bronze
            self.score_display.setStyleSheet('QLabel { color : '+ c.BRONZE + '; }')
        if (len(top3) >= 2 and score > top3[1].score) or len(top3) < 2: # Sollte der Aktuelle Score den allgemeinen 2. Platz bringen ist er silber
            self.score_display.setStyleSheet('QLabel { color : '+ c.SILVER + '; }')
        if (len(top3) >= 1 and score > top3[0].score) or len(top3) < 1: # Sollte der Aktuelle Score den allgemeinen 1. Platz bringen ist er gold
            self.score_display.setStyleSheet('QLabel { color : '+ c.GOLD + '; }')
        if score >= 10:
            self.score_display.setText(str(score))
        else:
            self.score_display.setText('0' + str(score))

    def paintEvent(self, e):
        painter = QPainter(self)
        if self.obj_arr[0] != None:
            self.draw_object(painter, self.obj_arr[0].x, self.obj_arr[0].y, self.obj_arr[0].color)
        self.draw_cars(painter, self.car_list)
        painter.end()

    def move(self, car):
        """ Bewegt das Auto (car) und prüft dabei ob ein Objekt eingesammelt wird oder
        das Auto mit sich selst oder der Wand kollidiert
        """
        try:
            car.move()
            if self.obj_arr[0] != None and self.obj_arr[0].collect(car):
                car.add_tail(10)
                self.score = self.score + 1
                self.update_score(self.score)
                self.obj_arr[0] = None
        except(expections.OutOfMapError, expections.SelfDestruction):
            self.print_out(self.big_out, 'Score: ' + str(self.score))
            if self.score > 0:
                self.highscore.add_score(self.c1.name, self.score)
            self.print_highscore(self.highscore)
            self.end()

    def timerEvent(self, e):
        if self.obj_arr[0] == None:     # immer wenn kein Ojekt auf dem Feld ist wird ein neues hinzugefügt
            self.obj_arr[0] = objects.Object(self.car_list, self.obj_arr, 0)
        self.cars_move(self.car_list)
        self.update()
