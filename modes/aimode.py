from random import random
from modes import multiplayermode
import constants as c
from constants import Directions as d

class AIMode(multiplayermode.LokMulti):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(c.START_X_4P_1, c.START_Y_4P_1, d.SOUTH, c.BLUE, True, c.PLAYER_NAME, 50)
        self.c2 = self.new_ai(c.START_X_4P_2, c.START_Y_4P_2, d.EAST, c.RED, True, 'AI', 50)
        self.c3 = self.new_ai(c.START_X_4P_3, c.START_Y_4P_3, d.WEST, c.RED, True, 'AI', 50)
        self.c4 = self.new_ai(c.START_X_4P_4, c.START_Y_4P_4, d.NORTH, c.RED, True, 'AI', 50)
        self.counter = 0
 
    def tail_detection(self, car, dir):
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
        if (dir == d.NORTH and car.y < 1) \
        or (dir == d.EAST and car.x > c.BOARD_WIDTH - 2) \
        or (dir == d.SOUTH and car.y > c.BOARD_HEIGHT - 2) \
        or (dir == d.WEST and car.x < 1):
            return True
        else:
            return False

    def car_detection(self, car, dir):
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
                if enemy.x == next_x and enemy.y == next_y and random() < 0.8:
                    return True
                tail_arr = enemy.get_tail()
                for i in tail_arr:
                    if i.x == next_x and i.y == next_y and random() < 0.8:
                        return True
        return False

    def get_info(self, car):
        map = [0, 0, 0, 0]
        i = 0
        while(i < 4):
            if(i != car.dir and (i + car.dir == 2 or i + car.dir == 4)):
                map[i] = -5
            elif self.tail_detection(car, i) or self.border_detection(car, i) or self.car_detection(car, i):
                map[i] = -1
            else:
                map[i] = 1
            i = i + 1
        return map

    def cars_move(self, car_list):
        for i in car_list:
            if i.ai:
                i.change_direction(self.get_info(i))
            else:
                i.change_direction()
            self.move(i)
