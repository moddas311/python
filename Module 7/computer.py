class CPU:
    def __init__(self, core) -> None:
        self.core = core 
        
class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HDD:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
   
# computer has a cpu 
# computer has ram
# computer has HDD capacity 
     
class Computer:
    def __init__(self, cores, ram_size, hdd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hdd_capacity = hdd_capacity
        

mac = Computer(8, 16, 512)