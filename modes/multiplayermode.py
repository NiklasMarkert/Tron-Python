from PyQt5.QtGui import QPainter, QColor
import constants as c
import expections
import board

class LokMulti(board.Board):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(30, 30, c.NORTH, c.BLUE, True, 'Player1', 50)
        self.c2 = self.new_car(60, 30, c.SOUTH, c.PINK, True, 'Player2', 50)
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
            self.print_out(self.big_out, car.name + ' lost!')
            self.end()

    def extra_length(self):
        self.counter = self.counter + 1
        if self.counter % 100 == 0:
             for i in self.car_list:
                 i.add_tail(10)

    def timerEvent(self, e):
        self.extra_length()
        self.cars_move(self.car_list)
        if self.c1.x == self.c2.x and self.c1.y == self.c2.y:   # Die Autos fahren gegeneinander
            self.print_out(self.big_out, 'Tie!')
            self.end()
        self.update()

