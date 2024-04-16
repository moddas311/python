# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Gadget:
    def __init__(self, brand, model, price, color, origin) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.origin = origin
        
    def run(self):
        return f'Running laptop{self.brand}'

class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
    
class Phone(Gadget):
    def __init__(self,brand, model, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, model, price, color, origin)
    
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'Phone: {self.brand} {self.model} {self.price} {self.color} {self.origin} {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
        
    def change_lance(self):
        pass
        

# inheritance 
my_phone = Phone('iTel+', 'S23+', 23900, 'Ocean Blue', 'China', True)
# print(my_phone.color)
print(my_phone)