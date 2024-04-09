class Shop:
    cart = [] # cart is clss attribute
    
    def __init__(self, buyer): # class attribute
        self.buyer = buyer
    
    def add_to_cart(self, item): # class method
        self.cart.append(item)
        
moddasir = Shop('Moddasir')
moddasir.add_to_cart('Laptop')
moddasir.add_to_cart('Phone')

print(moddasir.cart)

tamim = Shop('Tamim')
tamim.add_to_cart('Mobile')
tamim.add_to_cart('Panjabi')

print(tamim.cart)