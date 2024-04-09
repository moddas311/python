# Pen class create three objects with different instance atttribuute

class Pen():
    
    def __init__(self, owner, brand, price):
        self.owener = owner
        self.brand = brand
        self.price = price 
        
my_pen = Pen('Moddasir','Pin-Point', 6 )
her_pen = Pen('Hamida','Hi-School', 6 )
his_pen = Pen('Babu','All-Time', 8 )

print(my_pen.owener, my_pen.brand, my_pen.price)
print(her_pen.owener, her_pen.brand, her_pen.price)
print(his_pen.owener, his_pen.brand, his_pen.price)