from PyQt5.QtGui import QPainter, QColor
import constants as c
from constants import Directions as d
import expections
import board

class LokMulti(board.Board):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(c.START_X_2P_1, c.START_Y_2P_1, d.NORTH, c.BLUE, True, c.PLAYER_NAME, 50)
        self.c2 = self.new_car(c.START_X_2P_2, c.START_Y_2P_2, d.SOUTH, c.PINK, True, 'Player2', 50)
        self.counter = 0

    def paintEvent(self, e):
        painter = QPainter(self)
        self.draw_cars(painter, self.car_list)
        painter.end()

    def test_collision(self, car, enemy):
        tail_arr = enemy.get_tail()
        for i in tail_arr:
            if car.x == i.x and car.y == i.y:
                raise expections.Collision
                break

    def move(self, car):
        try:
            car.move(1)
            for i in self.car_list:
                if i != car:
                    self.test_collision(car, i)
        except (expections.OutOfMapError, expections.SelfDestruction, expections.Collision):
            car.lost = True

    def extra_length(self):
        self.counter = self.counter + 1
        if self.counter % 100 == 0:
             for i in self.car_list:
                 i.add_tail(10)

    def test_crash(self, car_list):
        for i in car_list:
            for j in car_list:
                if i is not j and i.x == j.x and i.y == j.y:
                    i.lost = True
                    j.lost = True
        alive = 0
        for i in car_list:
            if not i.lost:
                alive = alive + 1
                winner = i
                if alive >= 2:
                    break
        if alive == 0:
            self.print_out(self.big_out, 'Tie!')
            self.end()
        elif alive == 1:
            self.print_out(self.big_out, winner.name + ' won!')
            self.end()
        else:
            for i in car_list:
                if i.lost:
                    car_list.remove(i)

    def timerEvent(self, e):
        self.extra_length()
        self.cars_move(self.car_list)
        self.test_crash(self.car_list)
        self.update()

