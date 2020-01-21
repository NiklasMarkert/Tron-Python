import expections
import constants as c
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
    
    def move(self, amount):
        """ Lässt das Auto in die momentane Richtung dir bewegen
        Eingabe: amount = Angabe um wie viel sich das Auto bewegt
        """
        old_x = self.x
        old_y = self.y
        if self.dir == c.NORTH:
            self.y -= amount
        elif self.dir == c.EAST:
            self.x += amount
        elif self.dir == c.SOUTH:
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
            if new_dir == c.NORTH and self.dir != c.SOUTH:
                self.dir = c.NORTH
            elif new_dir == c.EAST and self.dir != c.WEST:
                self.dir = c.EAST
            elif new_dir == c.SOUTH and self.dir != c.NORTH:
                self.dir = c.SOUTH
            elif new_dir == c.WEST and self.dir != c.EAST:
                self.dir = c.WEST

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

