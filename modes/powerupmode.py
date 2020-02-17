from PyQt5.QtGui import QPainter
from random import random
from modes import aimode
from constants import Directions as d, Types as t, StartingPositions as s, Colors as c, Options as o, TYPE_TIMER
import expections
import objects

class PowerUp(aimode.AIMode):

    def __init__(self, multiplayer):
        super().__init__(1)
        self.counter = 0
        self.multiplayer = multiplayer

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(s.START_X_2P_1, s.START_Y_2P_1, d.NORTH, c.BLUE, o.PLAYER_NAME, 30)
        if self.multiplayer:
            self.c2 = self.new_car(s.START_X_2P_2, s.START_Y_2P_2, d.SOUTH, c.PINK, 'Player2', 30)
        else:
            self.c2 = self.new_ai(s.START_X_2P_2, s.START_Y_2P_2, d.SOUTH, c.RED, 'AI', 30)
        self.counter = 0
        self.powerup_1 = 0
        self.powerup_2 = 0
        self.obj_arr = [None, None]

    def move(self, car):
        """ Es wird ein Auto (car) bewegt, dabei wird geprüft ob es ein PowerUp einsammelt 
        oder mit der Mauer, sich selbst oder einem anderen Auto kollidiert
        """
        try:
            car.move()
            for i in range(len(self.obj_arr)):
                if self.obj_arr[i] != None and self.obj_arr[i].collect(car):
                    self.obj_arr[i].action(car)
                    self.obj_arr[i] = None
            for i in self.car_list:
                if i != car:
                    self.test_collision(car, i)
        except(expections.OutOfMapError, expections.SelfDestruction, expections.Collision):
            car.lost = True

    def update_object(self):
        """ Es werden falls nicht vorhanden passende PowerUps auf dem Spielfeld plaziert
        """
        # Es ist immer ein PowerUp des Typen PLUS_LENGTH auf dem Spielfeld und befindet sich immer in obj_arr[0]
        if self.obj_arr[0] == None: # Falls kein solches PowerUp vorhanden, wird sofort eins erzeugt
            self.obj_arr[0] = objects.Object(self.car_list, self.obj_arr, t.PLUS_LENGTH)
        if self.counter == 0:       # Jedes PowerUp, das in obj_arr[1] liegt, hat einen Timer, wenn dieser
            self.obj_arr[1] = None  # abgelaufen ist wird das PowerUp entfernt
        else:
          self.counter = self.counter - 1
        # In obj_arr[1] liegen die anderen PowerUps, jedoch muss nicht immer eins vorhanden sein
        if self.obj_arr[1] == None:
            if random() < 0.05: # mit einer Wahrscheinlichkeit von 5% wird ein neues PowerUp erzeugt, falls keines vorhanden ist
                r = random()
                if r < 0.35:                                        # 35%
                    type = t.MINUS_LENGTH
                    self.counter = TYPE_TIMER[t.MINUS_LENGTH]
                elif r < 0.70:                                      # 35%
                    type = t.DESTROY_TAIL
                    self.counter = TYPE_TIMER[t.DESTROY_TAIL]
                elif r < 0.82 and self.powerup_1 < 2:               # 12%, wird maximal zwei mal im Spiel gespawnt
                    type = t.SELFDMG_OF
                    self.counter = TYPE_TIMER[t.SELFDMG_OF]
                    self.powerup_1 = self.powerup_1 + 1
                elif r < 0.94 and r > 0.82 and self.powerup_2 < 2:   # 12%, wird maximal zwei mal im Spiel gespawnt
                    type = t.BORDERDMG_OF
                    self.counter = TYPE_TIMER[t.BORDERDMG_OF]
                    self.powerup_2 = self.powerup_2 + 1
                else:                                                # 6% (- 30%), erhöhte Wahrscheinlichkeit, falls SELFDMG_OF und/oder                                                    # BORDER
                    type = t.LOSE                                    # BORDERDMG_OF schon zwei mal gespawnt sind
                    self.counter = TYPE_TIMER[t.LOSE]
                self.obj_arr[1] = objects.Object(self.car_list, self.obj_arr, type)

    def timerEvent(self, e):
        self.update_object()
        self.cars_move(self.car_list)
        self.update_cars(self.car_list)
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        for i in self.obj_arr:
            if i != None:
                self.draw_object(painter, i.x, i.y, i.color)
        self.draw_cars(painter, self.car_list)
        painter.end()
