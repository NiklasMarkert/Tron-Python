from random import random
import constants as c
import car

class AI(car.Car):
    def __init__(self, x, y, dir, color, self_dest, player_name):
        super().__init__(x, y, dir, color, self_dest, player_name)

    def turn_right(self):
        self.dir = (self.dir + 1) % 4

    def turn_left(self):
        self.dir = (self.dir + 3) % 4

    def border_detection(self):
        while(True):
            if (self.dir == c.NORTH and self.y < 1) \
            or (self.dir == c.EAST and self.x > c.BOARD_WIDTH - 2) \
            or (self.dir == c.SOUTH and self.y > c.BOARD_HEIGHT - 2) \
            or (self.dir == c.WEST and self.x < 1):
                if random() > 0.5:
                    self.turn_right()
                else:
                    self.turn_left()
            else:
                break

    def change_direction(self):
        
        if random() < 0.1:
            if random() > 0.5:
                self.turn_right()
            else:
                self.turn_left()
        self.border_detection()


