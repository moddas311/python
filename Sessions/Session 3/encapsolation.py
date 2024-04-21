

class Shop:
    
    # products = [] # class attribute. jodi kokhono sob product ek jaigai store korar dorkar pore eivabe use hbe. 
    
    def __init__(self, name):
        self.name = name 
        self.products = [] # instance attribute
        self.__balance = 500  # private attribute and eitar nam holo access modifier 
        
    def __repr__(self) -> str:
        return f'This shop name is: {self.name}'
    
    def add_products(self, name, price):
        product =  Product(name, price)
        self.products.append(product)
        
    def sell_product(self, product):
        self.balance += product.price 
    
    # private method 
    def __tax_add(self):
        return self.__balance * 0.10
        
    def get_balance(self):
        return self.__balance - self.__tax_add()
    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __repr__(self) -> str:
        return self.name
        
    
shop_1 = Shop('Apple')
shop_1.add_products('iPhone 15', 89990)
shop_1.add_products('iPhone 15 Pro', 96790)
shop_1.add_products('iPhone 15 Pro Max', 119990)

shop_2 = Shop('Samsung')
shop_2.add_products('S24', 800000)
shop_2.add_products('S24 Plus', 950000)
shop_2.add_products('S24 Ultra', 146000)

print(shop_1.get_balance())