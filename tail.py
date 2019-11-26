#Repräsentation des Schweifes als verkettete Liste von Schweifobjekten ("TailParts")
class TailPart:
    
    #Konstruktor der Klasse Tail
    #
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.next = None
    
    def add_part(self):
        if self.next == None:
            self.next = TailPart(self.x, self.y, self.color)
        else:
           self.next.add_part()

    def move(self, x, y):
        oldX = self.x
        oldY = self.y
        self.x = x
        self.y =y

        if self.next != None:
            self.next.move(oldX, oldY)

    def get_tail(self, tail_arr):
        new_tail_arr = tail_arr + [self]
        
        if self.next != None:
            return self.next.get_tail(new_tail_arr)
        else:
            return new_tail_arr
            