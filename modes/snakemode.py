from PyQt5.QtGui import QPainter, QColor
import constants as c
import expections
import board
import objects

class SnakeMode(board.Board):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(c.BOARD_WIDTH / 2, c.BOARD_HEIGHT / 2, c.NORTH, c.BLUE, True, 'Player1', 20)
        self.obj_arr = [None]
        self.score = 0

    def draw_object(self, painter, x, y, color):
        color = QColor(color)
        painter.fillRect(x * c.FIELD_SIZE - c.FIELD_SIZE/2, y * c.FIELD_SIZE - c.FIELD_SIZE/2, 2 *  c.FIELD_SIZE, 2 * c.FIELD_SIZE, color)

    def paintEvent(self, e):
        painter = QPainter(self)
        if self.obj_arr[0] != None:
            self.draw_object(painter, self.obj_arr[0].x, self.obj_arr[0].y, self.obj_arr[0].color)
        self.draw_cars(painter, self.car_list)
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
        self.cars_move(self.car_list)
        self.update()
