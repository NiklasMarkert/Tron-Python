import Expections
import Tail

class Car:

    #Konstruktor der Klasse Car
    #Setzt die x- und y- Koordinate und die Startrichtung 
    def __init__(self, x, y, dir, color):
        self.x = x
        self.y = y
        self.dir = dir      # 'N' = North, 'E' = East, 'S' = South, 'W' = West
        self.color = color  # 1 = blue, 2 = lighter blue
        self.tail = Tail.TailPart(self.x, self.y, self.color + 1, self)
    
    #Lässt das Auto in die momentane Richtung dir bewegen
    #Eingabe: amount = Angabe um wie viel sich das Auto bewegt
    def move(self, amount):
        oldX = self.x
        oldY = self.y
        
        if self.dir == 'N':
            self.y -= amount
        elif self.dir == 'E':
            self.x += amount
        elif self.dir == 'S':
            self.y += amount
        else:                   # self.dir == 'W'
           self.x -= amount

        self.tail.move(oldX, oldY)

        if self.x > 90 or self.x < 0 or self.y > 60 or self.y < 0:
            raise Expections.OutOfMapError

    #Verändert die Richtung des Autos, nachdem es die Richtungsveränderung geprüft hat
    #Eingabe: newDir = Neue Richtung in die das Auto sich bewegen soll  
    def changeDirection(self, newDir):
        if newDir != self.dir:
            if newDir == 'N' and self.dir != 'S':
                self.dir = 'N'
            elif newDir == 'E' and self.dir != 'W':
                self.dir = 'E'
            elif newDir == 'S' and self.dir != 'N':
                self.dir = 'S'
            elif newDir == 'W' and self.dir != 'E':
                self.dir = 'W'

    def addTail(self, amount):
        for i in range(amount):
            self.tail.addPart()

    def getTail(self):
        tArr = []
        return self.tail.getTail(tArr)

