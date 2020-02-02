class Scoreobject:
    
    def add_object(self, name, score):
        if self.next == None:
            self.next = Scoreobject(name, score, None)
        elif self.next.score < score:
            self.next = Scoreobject(name, score, self.next)
        else:
            self.next.add_object(name, score)

    def print_out(self):
        print(self.name + " - " + str(self.score))
        if self.next != None:
            self.next.print_out()
    
    def get_scores(self, max, c, arr):
        if c + 1 >= max or self.next == None:
            return arr + [self]
        else:
            return self.next.get_scores(max, c + 1, arr + [self])

    def __init__(self, name, score, next):
        self.name = name
        self.score = score
        self.next = next




