from PyQt5.QtGui import QPainter, QColor
from constants import Directions as d, StartingPositions as s, Colors as c, Options as o
import expections
import board

class LokMulti(board.Board):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(s.START_X_2P_1, s.START_Y_2P_1, d.NORTH, c.BLUE, o.PLAYER_NAME, 50)
        self.c2 = self.new_car(s.START_X_2P_2, s.START_Y_2P_2, d.SOUTH, c.PINK, 'Player2', 50)
        self.counter = 0

    def paintEvent(self, e):
        painter = QPainter(self)
        self.draw_cars(painter, self.car_list)
        painter.end()

    def test_collision(self, car, enemy):
        """ Testet ob ein Auto (car) in den Schweif eines anderen Autos (enemy) fährt
        """
        tail_arr = enemy.get_tail()
        for i in tail_arr:
            if car.x == i.x and car.y == i.y:
                raise expections.Collision
                break

    def move(self, car):
        try:
            car.move()
            for i in self.car_list:
                if i != car:
                    self.test_collision(car, i)
        except (expections.OutOfMapError, expections.SelfDestruction, expections.Collision):
            car.lost = True

    def extra_length(self):
        """ Länge des Schweifes wird für beide Autos alle 100 Ticks verlängert 
        """
        self.counter = self.counter + 1
        if self.counter % 100 == 0:
             for i in self.car_list:
                 i.add_tail(10)

    def update_cars(self, car_list):
        """ Aktualliesiert den "Lebens-Status" der Autos und checkt ob es einen Gewinner gibt
        """
        # Für jedes Paar von zwei Autos wird gecheckt ob sie sich gegenseitig in den "Kopf" fahren
        # -> falls jahr wird bei beiden lost auf True gesetzt
        for i in car_list:
            for j in car_list:
                if i is not j and i.x == j.x and i.y == j.y:
                    i.lost = True
                    j.lost = True
        # Es werden alle Autos durchgegangen und geschaut wieviele noch leben
        alive = 0
        for i in car_list:
            if not i.lost:
                alive = alive + 1
                winner = i
                if alive >= 2:
                    break
        if alive == 0:      # Sollte keines mehr leben gibt es ein Unentschieden
            self.print_out(self.big_out, 'Tie!')
            self.end()
        elif alive == 1:    # Lebt nur noch eins, hat dieses gewonnen
            self.print_out(self.big_out, winner.name + ' won!')
            self.end()
        else:               # Leben noch mindestens 2, werden alle Autos die gestorben werden entfernt
            for i in car_list:
                if i.lost:
                    car_list.remove(i)
            # Es werden noch alle lebenden Autos durchgegangen und geschaut ob nur noch KI-Autos leben
            # -> Falls ja, wird das Spiel beendet und die KI generell als Gewinner gesehen
            only_ai = True
            for i in car_list:
                if not i.ai:
                    only_ai = False
                    break
            if only_ai:
                self.print_out(self.big_out, 'AI won!')
                self.end()


    def timerEvent(self, e):
        self.extra_length()
        self.cars_move(self.car_list)
        self.update_cars(self.car_list)
        self.update()

