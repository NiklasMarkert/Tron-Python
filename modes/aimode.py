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
 

