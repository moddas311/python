class Phone:
    manufactured = 'China'
    
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
    
    def send_SMS(self, phone, sms): # ekta perameter beshi dite hobe
        text = f'sending SMS to: {phone} and message: {sms}'
        return text
    
my_phone = Phone('Moddasir', 'SM-A-34', 29760)
print(my_phone.owner, my_phone.brand, my_phone.price)

tam_phone = Phone('Tamim', 'SM-A-54', 39760)
print(tam_phone.owner, tam_phone.brand, tam_phone.price)

my_txt = my_phone.send_SMS(154106282, 'Mon valo nei')
tam_txt = tam_phone.send_SMS(1516051992, 'Tamim Iqbal waw')

print(my_txt)
print(tam_txt)