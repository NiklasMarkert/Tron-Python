import expections
import constants as c
from constants import Directions as d, BoardSize as b
from player import tail


class Car:

    def __init__(self, x, y, dir, color, player_name):
        """ Konstruktor der Klasse Car
        """
        self.x = x  
        self.y = y                          
        self.dir = dir                      # NORTH/EAST/SOUTH/WEST
        self.next_dir = dir
        self.color = color[0]
        self.tail = tail.TailPart(self.x, self.y, color[1])
        self.name = player_name
        self.self_destruction = True        # True = Man verliert wenn man in den eigenen Schweif fährt, False = Man verliert nicht
        self.border_destruction = True      # True = Man verliert wenn gegen die Border fährt, False = Man verliert nicht
        self.ai = False
        self.lost = False
    
    def move(self):
        """ Lässt das Auto in die momentane Richtung dir bewegen
        """
        old_x = self.x
        old_y = self.y
        if self.dir == d.NORTH:
            self.y -= 1
        elif self.dir == d.EAST:
            self.x += 1
        elif self.dir == d.SOUTH:
            self.y += 1
        else:                   # self.dir == WEST  
           self.x -= 1
        self.tail.move(old_x, old_y)
        if self.x > b.BOARD_WIDTH - 1 or self.x < 0 or self.y > b.BOARD_HEIGHT - 1 or self.y < 0:
            if self.border_destruction:
                raise expections.OutOfMapError
            else:
                self.x = self.x % b.BOARD_WIDTH
                self.y = self.y % b.BOARD_HEIGHT
        if self.self_destruction:
            tail_arr = self.get_tail()
            for i in tail_arr:
                if self.x == i.x and self.y == i.y:
                    raise expections.SelfDestruction

    def change_direction(self):
        """ Verändert die Richtung des Autos, nachdem es die Richtungsveränderung geprüft hat
        """
        new_dir = self.next_dir
        if new_dir != self.dir:
            if new_dir == d.NORTH and self.dir != d.SOUTH:
                self.dir = d.NORTH
            elif new_dir == d.EAST and self.dir != d.WEST:
                self.dir = d.EAST
            elif new_dir == d.SOUTH and self.dir != d.NORTH:
                self.dir = d.SOUTH
            elif new_dir == d.WEST and self.dir != d.EAST:
                self.dir = d.WEST

    def get_tail(self):
        """ Gibt den Schweif des Autos aus
        Ausgabe: Array in dem alle Schweifobjekte des Autos gespeichert sind
        """
        tail_arr = []
        return self.tail.get_tail(tail_arr)

    def add_tail(self, amount):
        """ Fügt dem Auto einen Schweif hinzu, bzw. verlängert ihn
        Eingabe: amount = Angabe umwieviel Einheiten der Schweif verlängert werden soll
        """
        for i in range(amount):
            self.tail.add_part()

    def remove_tail(self, amount):
        """ Entfernt einen Teil des Schweifs
        Eingabe: amount = Angabe wieviele Einheiten des Schweifs entfernt werden sollen
        """
        tail_arr = self.get_tail()
        size = len(tail_arr)
        if amount >= size:
            amount = size - 1
        counter = size - amount - 1
        self.tail.remove_parts(counter)
    


