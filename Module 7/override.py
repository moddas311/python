class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name 
        self.age = age 
        self.height = height
        self.weight = weight
        
    def eat(self):
        print('Every person should eat healthy food.')
        
    def exercise(self):
        raise NotImplementedError
        
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # override   
    def eat(self):
        print('Every Player should eat vegetables')
        
    def exercise(self):
        print('Players should go to gym everyday.')
     
    # + sign operator overload   
    def __add__(self, other):
        return self.age + other.age
    
    # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    # > operator overload  
    def __gt__(self, other):
        return self.age > other.age 

shakib = Cricketer('Shakib Al Chor', 32, 5, 68, 'Bangladesh')
musfiqur = Cricketer('Musfiqur Rahim', 34, 5, 59, 'Banglades')

# shakib.eat()
# shakib.exercise()

# Plus sign overload
print(63+58)
print('shakib' + 'Rakib')
print([12, 98] + [5, 6, 7, 1, 2])

print(shakib + musfiqur)
print(shakib * musfiqur)
print(len(shakib))
print(shakib > musfiqur)