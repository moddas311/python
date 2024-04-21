                            #----------------simple inheritance---------------------# 

# superior class 
class Vehicle:
    def __init__(self, vehicle_type, brand, model):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        
# sub class     
class Car(Vehicle):
    def __init__(self, vehicle_type, brand, model, capacity):
        self.capacity = capacity
        super().__init__(vehicle_type, brand, model)
        
    def __repr__(self):
        return f'Type: {self.vehicle_type}\n Brand: {self.brand}\n Model: {self.model}\n Capacity: {self.capacity}'
    
cycle = Car('Cycle', 'Hero', 'H-12', 1)
print(cycle) 



                            #----------------multi-level inheritance---------------------#
                           
# superior class 
class Vehicle:
    def __init__(self, vehicle_type, brand, model):
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.model = model
        
# sub class     
class Car(Vehicle):
    def __init__(self, vehicle_type, brand, model, capacity):
        self.capacity = capacity
        super().__init__(vehicle_type, brand, model)

class Electric_car(Car):
    def __init__(self, vehicle_type, brand, model, capacity, battery):
        self.battery = battery
        super().__init__(vehicle_type, brand, model, capacity)
        
Tesla = Electric_car('Private Car', 'Tesla', 'E-76', 4, '8000mAh')
print(Tesla.model)



                           #----------------multiple inheritance---------------------#
class Watch:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_time(self):
        print('Displaying Time')
    
    
class Fitness_tracker:
    def __init__(self, price):
        self.price = price    
    
    def track_step(self):
        print('Tracking step')

    def track_calories(self):
        print('Tracking calories')
        
class smart_watch(Watch, Fitness_tracker):
    def __init__(self, brand, model, price):
        Watch.__init__(self, brand, model)
        Fitness_tracker.__init__(self, price)
        
    def display(self):
        print('Display okay!')
        
apple = smart_watch('Apple', 'Series 4', 25000)
apple.track_step()
apple.track_calories()
apple.display_time()