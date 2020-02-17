from random import random
from modes import multiplayermode
from constants import Directions as d, StartingPositions as s, Colors as c, Options as o, BoardSize as b, AI_DIR

class AIMode(multiplayermode.LokMulti):

    def __init__(self, amount_bots):
        super().__init__()
        if amount_bots < 1:
            self.amount_bots = 1
        elif amount_bots > 3:
            self.amount_bots = 3
        else:
            self.amount_bots = amount_bots

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(s.START_X[0], s.START_Y[0], d.SOUTH, c.BLUE, o.PLAYER_NAME, 50)
        for i in range(self.amount_bots):
            self.ai = self.new_ai(s.START_X[i+1], s.START_Y[i+1], AI_DIR[i], c.RED, 'AI', 50)
        self.counter = 0
 
    def tail_detection(self, car, dir):
        """ Prüft ob das Auto (car) mit seinem eigenen Schweif kollidieren würde, 
        wenn es sich in eine gegebene Richtung (dir) bewegt
        True: wenn Ja
        """
        next_x = car.x
        next_y = car.y
        if dir == d.NORTH:
            next_y = next_y - 1
        elif dir == d.EAST:
                next_x = next_x + 1
        elif dir == d.SOUTH:
            next_y = next_y + 1
        else:                       # dir == WEST
            next_x = next_x - 1
        tail_arr = car.get_tail()
        for i in tail_arr:
            if i.x == next_x and i.y == next_y:
                return True
        return False

    def border_detection(self, car, dir):
        """ Prüft ob das Auto (car) mit der Wand kollidieren würde, 
        wenn es sich in eine gegebene Richtung (dir) bewegt
        True: wenn Ja
        """
        if (dir == d.NORTH and car.y < 1) \
        or (dir == d.EAST and car.x > b.BOARD_WIDTH - 2) \
        or (dir == d.SOUTH and car.y > b.BOARD_HEIGHT - 2) \
        or (dir == d.WEST and car.x < 1):
            return True
        else:
            return False

    def car_detection(self, car, dir):
        """ Prüft ob das Auto (car) mit einem anderen Auto kollidieren würde, 
        wenn es sich in eine gegebene Richtung (dir) bewegt
        True: wenn Ja
        """
        next_x = car.x
        next_y = car.y
        if dir == d.NORTH:
            next_y = next_y - 1
        elif dir == d.EAST:
                next_x = next_x + 1
        elif dir == d.SOUTH:
            next_y = next_y + 1
        else:                       # dir == WEST
            next_x = next_x - 1
        for enemy in self.car_list:
            if enemy is not car:
                if enemy.x == next_x and enemy.y == next_y and random() < 0.8: # KI weicht mit 80%iger Wahrscheinlichkeit dem Gegner aus
                    return True
                tail_arr = enemy.get_tail()
                for i in tail_arr:
                    if i.x == next_x and i.y == next_y and random() < 0.8: # KI weicht mit 80%iger Wahrscheinlichkeit dem Gegner aus
                        return True
        return False

    def get_info(self, car):
        """ Es wird ein Array erzeugt, in dem der Status steht, ob eine Richtung befahrbar ist oder nicht
        """
        map = [True, True, True, True]
        i = 0
        while(i < 4):
            if(i != car.dir and (i + car.dir == 2 or i + car.dir == 4)): # Entgegengesetzte Richtung zur aktuellen Richtung
                map[i] = False
            elif self.tail_detection(car, i) or self.border_detection(car, i) or self.car_detection(car, i):
                map[i] = False
            else:
                map[i] = True
            i = i + 1
        return map

    def cars_move(self, car_list):
        for i in car_list:
            if i.ai:
                i.change_direction(self.get_info(i))
            else:
                i.change_direction()
            self.move(i)
