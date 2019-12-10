from PyQt5.QtGui import QPainter, QColor
import constants as c
import expections
import car
import board
import objects

class LokMulti(board.Board):

    def __init__(self):
        super().__init__()

    def start(self):
        self.next_dir1 = 'N'
        self.c1 = car.Car(30, 30, 'N', c.BLUE, True, 'Player1')
        self.c1.add_tail(50)
        self.next_dir2 = 'S'
        self.c2 = car.Car(60, 30, 'S', c.PINK, True, 'Player2')
        self.c2.add_tail(50)

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
            self.print_out(self.big_out, car.name + ' lost!')
            self.end()

    def timerEvent(self, e):
        self.c1.change_direction(self.next_dir1)
        self.c2.change_direction(self.next_dir2)
        self.move(self.c1, self.c2)
        self.move(self.c2, self.c1)
        if self.c1.x == self.c2.x and self.c1.y == self.c2.y:   # Die Autos fahren gegeneinander
            self.print_out(self.big_out, 'Tie!')
            self.end()
        self.update()


class SnakeMode(board.Board):

    def __init__(self):
        super().__init__()

    def start(self):
        self.next_dir1 = 'N'
        self.c1 = car.Car(45, 30, 'N', c.BLUE, True, 'Player1')
        self.c1.add_tail(20)
        self.obj_arr = [None]
        self.score = 0

    def draw_object(self, painter, x, y, color):
        color = QColor(color)
        painter.fillRect(x * c.FIELD_SIZE - c.FIELD_SIZE/2, y * c.FIELD_SIZE - c.FIELD_SIZE/2, 2 *  c.FIELD_SIZE, 2 * c.FIELD_SIZE, color)

    def paintEvent(self, e):
        painter = QPainter(self)
        if self.obj_arr[0] != None:
            self.draw_object(painter, self.obj_arr[0].x, self.obj_arr[0].y, self.obj_arr[0].color)
        self.draw_tail(self.c1, painter)
        self.draw_square(painter, self.c1.x, self.c1.y, self.c1.color)
        painter.end()

    def move(self, car):
        try:
            car.move(1)
            self.obj_arr[0].collect(car)
        except(expections.OutOfMapError, expections.SelfDestruction):
            self.print_out(self.big_out, 'Score: ' + str(self.score))
            self.end()
        except(expections.Collected):
            car.add_tail(10)
            self.score = self.score + 1
            self.obj_arr[0] = None

    def timerEvent(self, e):
        if self.obj_arr[0] == None:     # immer wenn kein Ojekt auf dem Feld ist wird ein neues hinzugefügt
            self.obj_arr[0] = objects.Object(self.c1, c.GREEN)
        self.c1.change_direction(self.next_dir1)
        self.move(self.c1)
        self.update()
