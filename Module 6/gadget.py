class Laptop:
    def __init__(self, model, brand, price, color, memory) -> None:
        self.model = model
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
    
    def run(self):
        return f'Running laptop{self.brand}'
    
    def coding(self):
        return 'learning python and practicing'
    
class Phone:
    def __init__(self, model, brand, price, color, dual_sim) -> None:
        self.model = model
        self.brand = brand 
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
        
    def run(self):
        return f'All the day using phone!'
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    
class Camera:
    def __init__(self, model, brand, price, color, pixel) -> None:
        self.model = model
        self.brand = brand
        self.price = price 
        self.color = color 
        self.pixel = pixel
        
    def run(self):
        pass
    
    def change_lance(self):
        pass
        