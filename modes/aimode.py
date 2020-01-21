from random import random
from modes import multiplayermode
import constants as c

class AIMode(multiplayermode.LokMulti):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(30, 30, c.NORTH, c.BLUE, True, 'Player1', 50)
        self.c2 = self.new_ai(60, 30, c.SOUTH, c.RED, True, 'Player2', 50)
        self.counter = 0
 
    def tail_detection(self, car, dir):
        next_x = car.x
        next_y = car.y
        if dir == c.NORTH:
            next_y = next_y - 1
        elif dir == c.EAST:
                next_x = next_x + 1
        elif dir == c.SOUTH:
            next_y = next_y + 1
        else:
            next_x = next_x - 1
        tail_arr = car.get_tail()
        for i in tail_arr:
            if i.x == next_x and i.y == next_y:
                return True
        return False

    def border_detection(self, car, dir):
        if (dir == c.NORTH and car.y < 1) \
        or (dir == c.EAST and car.x > c.BOARD_WIDTH - 2) \
        or (dir == c.SOUTH and car.y > c.BOARD_HEIGHT - 2) \
        or (dir == c.WEST and car.x < 1):
            return True

    def get_info(self, car):
        map = [0, 0, 0, 0]
        i = 0
        while(i < 4):
            if(i != car.dir and (i + car.dir == 2 or i + car.dir == 4)):
                map[i] = -5
            elif self.tail_detection(car, i) or self.border_detection(car, i):
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
