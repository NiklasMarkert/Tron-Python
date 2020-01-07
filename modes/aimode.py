from random import random
from modes import multiplayermode
import constants as c

class AIMode(multiplayermode.LokMulti):

    def __init__(self):
        super().__init__()

    def start(self):
        self.car_list = []
        self.c1 = self.new_car(30, 30, 'N', c.BLUE, True, 'Player1', 50)
        self.c2 = self.new_ai(60, 30, 'S', c.RED, True, 'Player2', 50)

    
    def border_detection(self):
        while(True):
            if self.c2.next_dir == 'N' and self.c2.y < 2:
                if random() > 0.5:
                     self.c2.next_dir = 'E'
                else:
                    self.c2.next_dir = 'W'
            elif self.c2.next_dir == 'E' and self.c2.x > c.BOARD_WIDTH - 3:
                if random() > 0.5:
                    self.c2.next_dir = 'S'
                else:
                    self.c2.next_dir = 'N'
            elif self.c2.next_dir == 'S' and self.c2.y > c.BOARD_HEIGHT - 3:
                if random() > 0.5: 
                    self.c2.next_dir = 'W'
                else:
                    self.c2.next_dir = 'E'
            elif self.c2.next_dir == 'W' and self.c2.x < 2:
                if random() > 0.5:
                    self.c2.next_dir = 'N'
                else:
                    self.c2.next_dir = 'S'
            else:
                break


