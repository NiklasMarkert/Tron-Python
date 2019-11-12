class TailPart:

    def __init__(self, x, y, color, last):
        self.x = x
        self.y = y
        self.color = color
        self.last = last
        self.next = None
    
    def addPart(self):
        if self.next == None:
            self.next = TailPart(self.x, self.y, self.color, self)
        else:
           self.next.addPart()

    def move(self, x, y):
        oldX = self.x
        oldY = self.y
        self.x = x
        self.y =y

        if self.next != None:
            self.next.move(oldX, oldY)

    def getTail(self, tArr):
        newTArr = tArr + [self]
        
        if self.next != None:
            return self.next.getTail(newTArr)
        else:
            return newTArr
            