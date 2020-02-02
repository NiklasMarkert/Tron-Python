import expections
import constants as c
from constants import Directions as d
import tail


class Car:

    def __init__(self, x, y, dir, color, self_dest, player_name):
        """ Konstruktor der Klasse Car
        Setzt die x- und y- Koordinate, die Startrichtung, die Farbe, die "Selbstzerstörungs"-Option,
        den Schweif und den Spielernamen
        """
        self.x = x
        self.y = y
        self.dir = dir                          # 'N' = North, 'E' = East, 'S' = South, 'W' = West
        self.next_dir = dir
        self.color = color[0]
        self.self_destruction = self_dest       # True = Man verliert wenn man in den eigenen Schweif fährt, False = Man verliert nicht
        self.tail = tail.TailPart(self.x, self.y, color[1])
        self.name = player_name
        self.ai = False
        self.lost = False
    
    def move(self, amount):
        """ Lässt das Auto in die momentane Richtung dir bewegen
        Eingabe: amount = Angabe um wie viel sich das Auto bewegt
        """
        old_x = self.x
        old_y = self.y
        if self.dir == d.NORTH:
            self.y -= amount
        elif self.dir == d.EAST:
            self.x += amount
        elif self.dir == d.SOUTH:
            self.y += amount
        else:                   # self.dir == WEST  
           self.x -= amount
        self.tail.move(old_x, old_y)
        if self.x > c.BOARD_WIDTH - 1 or self.x < 0 or self.y > c.BOARD_HEIGHT - 1 or self.y < 0:
          raise expections.OutOfMapError
        if self.self_destruction:
            tail_arr = self.get_tail()
            for i in tail_arr:
                if self.x == i.x and self.y == i.y:
                    raise expections.SelfDestruction

    def change_direction(self):
        """ Verändert die Richtung des Autos, nachdem es die Richtungsveränderung geprüft hat
        Eingabe: newDir = Neue Richtung in die das Auto sich bewegen soll  
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

    def add_tail(self, amount):
        """ Fügt dem Auto einen Schweif hinzu, bzw. verlängert ihn
        Eingabe: amount = Angabe umwieviel Einheiten der Schweif verlängert werden soll
        """
        for i in range(amount):
            self.tail.add_part()
    
    def get_tail(self):
        """ Gibt den Schweif des Autos aus
        Ausgabe: Array in dem alle Schweifobjekte des Autos gespeichert sind
        """
        tail_arr = []
        return self.tail.get_tail(tail_arr)

