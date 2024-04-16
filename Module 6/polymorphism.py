# poly --> many(multiple)
# morph --> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name 
    
    def make_sound(self):
        print('Animal making some sound!')
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def make_sound(self):
        print('Meow meow')
        
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('Gheu Gheu')
        
class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def make_sound(self):
        print('Mee Mee')

don = Cat('Real Don')
don.make_sound()

shephard = Dog('shephard')
shephard.make_sound()

mess = Goat('LM')
mess.make_sound()

animals = [don, shephard, mess]
for animal in animals:
    animal.make_sound()