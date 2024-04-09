class Shop:
    shopping_mall = 'Jamuna'
    
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #cart is an instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)
        
sanjit = Shop('Sanjit')
sanjit.add_to_cart('Pant')
sanjit.add_to_cart('Panjabi')
sanjit.add_to_cart('Lungi')
sanjit.add_to_cart('Gamcha')

junaid = Shop('Junaid')
junaid.add_to_cart('Juta')
junaid.add_to_cart('Mobile')

arnob = Shop('Arnob')
arnob.add_to_cart('Muri')
arnob.add_to_cart('Chop')
arnob.add_to_cart('begoni')

print(sanjit.buyer, sanjit.cart)
print(junaid.buyer, junaid.cart)
print(arnob.buyer, arnob.cart)