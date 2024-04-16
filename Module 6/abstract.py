from abc import ABC, abstractmethod

# abstract base class
class Animal(ABC):
    
    @abstractmethod # enforce all derived class to have a eat method 
    def eat(self):
        print('I need food')
        
        
    @abstractmethod # enforce all derived class to have a move method 
    def move(self):
        print('Wow!, it\'s moving')

class Monkey(Animal):
    
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name 
        super().__init__()
    
    def eat(self):
        print('Hey nana!, i am eating banana')
    
    def move(self):
        print('Pera')

layka = Monkey('Lucy')
layka.eat()