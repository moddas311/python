class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
        
    def remove_item(self, item):
        pass
        
    def checkout(self, amout):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        
        if amout < total:
            print(f'Please provide {total - amout} more')
            
        else:
            extra =  amout - total
            print(f'Here is your items and extra money: {extra}')
        
Junaid = Shopping("Junaid")

Junaid.add_to_cart('Panjabi', 1990, 1)
Junaid.add_to_cart('Juta', 2990, 1)
Junaid.add_to_cart('Jursey', 600, 1)

print(Junaid.cart)
Junaid.checkout(6000)