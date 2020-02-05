from random import random
import constants as c
import car

class AI(car.Car):
    def __init__(self, x, y, dir, color, self_dest, player_name):
        super().__init__(x, y, dir, color, self_dest, player_name)
        self.ai = True
        self.lastTurns = [0, 0]
        self.turns = 0

    def turn_right(self):
        self.dir = (self.dir + 1) % 4

    def turn_left(self):
        self.dir = (self.dir + 3) % 4

    def change_direction(self, map):
        r = random()
        if map[self.dir] < 0 or r < 0.05:
            if self.lastTurns[0] == self.lastTurns[1]:
                if self.lastTurns[0] == 1 and map[(self.dir + 3) % 4] > 0:
                    self.turn_left()
                    self.lastTurns[self.turns] = 2
                    self.turns = (self.turns+1)%2
                    return
                elif map[(self.dir + 1) % 4] > 0:
                    self.turn_right()
                    self.lastTurns[self.turns] = 1
                    self.turns = (self.turns+1)%2
                    return
            r = random()
            if r < 0.5:
                if map[(self.dir + 1) % 4] > 0:
                    self.turn_right()
                    self.lastTurns[self.turns] = 1
                    self.turns = (self.turns+1)%2
                elif map[(self.dir + 3) % 4] > 0:
                    self.turn_left()
                    self.lastTurns[self.turns] = 2
                    self.turns = (self.turns+1)%2
            else:
                if map[(self.dir + 3) % 4] > 0:
                    self.turn_left()
                    self.lastTurns[self.turns] = 2
                    self.turns = (self.turns+1)%2
                elif map[(self.dir + 1) % 4] > 0:
                    self.turn_right()
                    self.lastTurns[self.turns] = 1
                    self.turns = (self.turns+1)%2



