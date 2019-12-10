class TailPart:
    """ Repräsentation des Schweifes als verkettete Liste von Schweifobjekten ("TailParts")
    """
    
    def __init__(self, x, y, color):
        """ Konstruktor der Klasse TailPart
        Setzt die x- und y-Koordinate und die Farbe des Schweifobjekts
        """
        self.x = x
        self.y = y
        self.color = color
        self.next = None
    
    def add_part(self):
        """ Fügt ein Schweifobjekt am Ende des Schweifes hinzu
        """
        if self.next == None:
            self.next = TailPart(self.x, self.y, self.color)
        else:
           self.next.add_part()

    def move(self, x, y):
        """ Bewegt ein Schweifobjekt
        Eingabe: x- und y- Koordinate des vorhegenden Schweifobjekts, 
        welche die neuen Koordinaten dieses Objekts werden
        """
        oldX = self.x
        oldY = self.y
        self.x = x
        self.y =y
        if self.next != None:
            self.next.move(oldX, oldY)

    def get_tail(self, tail_arr):
        """ Rekursive Funktion, um den Schweif als Array zurückzugeben
        """
        new_tail_arr = tail_arr + [self]
        if self.next != None:
            return self.next.get_tail(new_tail_arr)
        else:
            return new_tail_arr
            