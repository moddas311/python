# Ena poribohon

class Company:
    def __init__(self, name, address) -> None:
        self.name = name 
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisor = []
        self.fare = []

class Driver:
    def __init__(self, name, license, age) -> None:
        self.name = name
        self.license = license
        self.age = age
        
class Counter:
    def __init__(self) -> None:
        pass
    
    def parchesr_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

Laal = Driver('Laal Miah', 13216511231, 26)