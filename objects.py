from random import randint
from constants import Types as t, BoardSize as b, Colors as c
import expections

class Object:

    def fits_car(self, car, x, y):
        """ Prüft ob gegebene Koordinaten (x, y) mit dem üergebenen Auto (car) kollidieren
        True: Falls nicht, False: Falls schon
        """
        if abs(car.x - x) <= 1 and abs(car.y - y) <= 1:
            return False
        tail_arr = car.get_tail()
        for i in tail_arr:
            if abs(i.x - x) <= 1 and abs(i.y - y) <= 1:
                return False
        return True

    def fits_obj(self, obj, x, y):
        """ Prüft ob gegebene Koordinaten (x, y) mit dem üergebenen Objekt (obj) kollidieren
        True: Falls nicht, False: Falls schon
        """
        if abs(obj.x - x) <= 5 and abs(obj.y - y) <= 5:
            return False
        else:
            return True

    def check_loc(self, cars, objects, x, y):
        """ Prüft ob gegebene Koordinaten (x, y) mit irgendeinem Auto aus cars oder Objekt aus objects kollidieren
        True: Falls nicht, False: Falls schon
        """
        for i in cars:
            if not self.fits_car(i, x, y):
                return False
        for i in objects:
            if i != None and not self.fits_obj(i, x, y):
                return False
        return True

    def find_loc(self, cars, objects):
        """ Generiert solange zufällige Positionen auf dem Board, bis eine mit keine Auto und keinem Objekt kollidiert 
        """
        while True:
            test_x = randint(1, b.BOARD_WIDTH - 2)
            test_y = randint(1, b.BOARD_HEIGHT - 2)
            if self.check_loc(cars, objects, test_x, test_y):
                self.x = test_x
                self.y = test_y
                return

    def collect(self, car):
        """ Prüft ob ein gegebenes Auto (car) das Objekt einsammelt
        True: Sammelt es ein, False: Wenn nicht
        """
        if abs(car.x - self.x) <= 1 and abs(car.y - self.y) <= 1:
            return True
        else:
            return False

    def action(self, car):
        """ Führt die Aktion aus, wenn das Objekt eingesammelt wird 
        """
        if self.type == t.PLUS_LENGTH:
            car.add_tail(10)                # eigener Schweif wird verlägnert
        elif self.type == t.MINUS_LENGTH:
            car.remove_tail(15)             # eigener Schweif wird verkürtzt
        elif self.type == t.SELFDMG_OF:
            car.self_destruction = False    # das einsammelnte Auto stribt nicht mehr, wenn ein es in sich selbst fährt
        elif self.type == t.DESTROY_TAIL:
            for i in self.cars:
                if i is not car:
                    i.remove_tail(10)       # der Schweif aller Gegner wird verkürtzt
        elif self.type == t.LOSE:
            car.lost = True                 # das einsammelnte Auto stirbt
        elif self.type == t.BORDERDMG_OF:   
            car.border_destruction = False  # das einsammelnte Auto stribt nicht mehr, wenn ein es in die Wand fährt
                                            # sodern kommt auf der anderen Seite wieder raus

    def __init__(self, cars, objects, type):
        self.find_loc(cars, objects)
        self.color = c.OBJECT_COLOR[type]
        self.type = type
        self.cars = cars
