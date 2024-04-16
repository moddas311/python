class Family:
    def __init__(self, address) -> None:
        self.address = address
    
class School:
    def __init__(self, id, current_class) -> None:
        self.id = id
        self.current_class = current_class
    
class Sports:
    def __init__(self, game) -> None:
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, address, id, current_class, game) -> None:
        Family.__init__(self, address)
        School.__init__(self, id, current_class)
        Sports.__init__(self, game)