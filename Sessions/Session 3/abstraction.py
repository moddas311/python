
# jodi kono project method must lagbe tokhn abstract class use kora lagbe cz 
# # abstract class baddho kore method use korte 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
         pass
     
class Rectangle(Shape):
    def __init__(self, length, width): 
        self.length = length 
        self.width = width 
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.1416 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.1416 * self.radius
    
rect = Rectangle(3, 4)
print('Rectangle area:', rect.area())
print('Rectangle perimeter:', rect.perimeter())

cir = Circle(5)
print('Circle area:', cir.area())
print('Circle perimeter:', cir.area())