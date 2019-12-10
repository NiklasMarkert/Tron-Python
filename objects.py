from random import randint
import constants as c
import expections

class Object:

    def fits(self, car, x, y):
        if abs(car.x - x) <= 1 and abs(car.y - y) <= 1:
            return False
        tail_arr = car.get_tail()
        for i in tail_arr:
            if abs(i.x - x) <= 1 and abs(i.y - y) <= 1:
                return False
        return True

    def find_loc(self, car):
        location = False
        while location is False:
            test_x = randint(1, c.BOARD_WIDTH - 2)
            test_y = randint(1, c.BOARD_HEIGHT - 2)
            if self.fits(car, test_x, test_y):
                self.x = test_x
                self.y = test_y
                location = True

    def collect(self, car):
        if abs(car.x - self.x) <= 1 and abs(car.y - self.y) <= 1:
            raise expections.Collected
    
    def __init__(self, car, color):
        self.find_loc(car)
        self.color = color
