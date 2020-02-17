from random import random
from player import car

class AI(car.Car):
    def __init__(self, x, y, dir, color, player_name):
        super().__init__(x, y, dir, color, player_name)
        self.ai = True
        self.lastTurns = [0, 0] # Array in dem die letzten zwei Drehungen gespeichert werden (rechts = 1/links = 2)
        self.turns = 0

    def turn_right(self):
        """ Dreht das Auto nach rechts
        """
        self.dir = (self.dir + 1) % 4

    def turn_left(self):
        """ Dreht das Auto nach links
        """
        self.dir = (self.dir + 3) % 4

    def change_direction(self, map):
        """ Nimmt die Bewegungen für die AI vor
        Eingabe: map = Array der Länge 4 in dem für jede Fahrtrichtung ein
        boolean Wert gespeichert ist, ob diese Richtung "befahrbar" ist (= True)
        oder nicht (= False)
        """
        r = random()
        if not map[self.dir] or r < 0.02:   # Falls jetzige Richtung nicht befahrbar oder mit einer 2% Wahrscheinlichkeit wird die Richtung geändert
            if self.lastTurns[0] == self.lastTurns[1]:                  # Falls die letzen zwei Truns in die selbe Richtung waren,
                if self.lastTurns[0] == 1 and map[(self.dir + 3) % 4]:  # wird versucht diesmal in die andere Richtung zu drehen
                    self.turn_left()
                    self.lastTurns[self.turns] = 2
                    self.turns = (self.turns+1)%2
                    return
                elif map[(self.dir + 1) % 4]:
                    self.turn_right()
                    self.lastTurns[self.turns] = 1
                    self.turns = (self.turns+1)%2
                    return
            r = random()
            if r < 0.5:     # 50% Wahrscheinlichtkeit für eine Rechtsdrehung, falls möglich
                if map[(self.dir + 1) % 4]:
                    self.turn_right()
                    self.lastTurns[self.turns] = 1
                    self.turns = (self.turns+1)%2
                elif map[(self.dir + 3) % 4]:
                    self.turn_left()
                    self.lastTurns[self.turns] = 2
                    self.turns = (self.turns+1)%2
            else:           # ansonsten Linksdrehung, falls möglich
                if map[(self.dir + 3) % 4]:
                    self.turn_left()
                    self.lastTurns[self.turns] = 2
                    self.turns = (self.turns+1)%2
                elif map[(self.dir + 1) % 4]:
                    self.turn_right()
                    self.lastTurns[self.turns] = 1
                    self.turns = (self.turns+1)%2



