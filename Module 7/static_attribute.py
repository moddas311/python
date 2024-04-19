# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod 
# differences between static method and class method 

class Shopping:
    cart = [] # class attribute class attribute 
    origin = 'China'
    
    def __init__(self, name, location) -> None:
        # instance attribute 
        self.name = name # Jamuna Future park
        self.location = location # Dhaka 
        
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')
        
    @staticmethod
    def multiply(a, b): #static method e self er kono dorkar nai 
        result = a * b
        print(result)
       
    @classmethod 
    def hudai(self, item): 
        print('Hudai ghuri kinar teka nai free free acr batas khaite alam', item)
        
basundhara = Shopping('Basundhara Shopping Complex', 'Panthopath Dhaka')
basundhara.purchase('Jeans', 1700, 2000)

# Shopping.purchase('Jeans', 1700, 2000, 900)
# basundhara.hudai('Shirt')
Shopping.hudai('Jeans')

Shopping.multiply(10, 10)
basundhara.multiply(4, 5)