def call():
    print('call someone i don\'t know' )
    return 'call done'

class Phone:
    price = 34450 
    color = 'Black'
    brand = 'Samsung'
    features = ['Camera', 'Dual Speaker', 'HD+ Display', '5G LTE']
    
    def call(self): # ekta perameter beshi dite hobe
        print('Calling one person')
        
    def send_SMS(self, phone, sms): # ekta perameter beshi dite hobe
        text = f'sending SMS to: {phone} and message: {sms}'
        return text
        

call()
my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_SMS(42577, 'I forgot to missed to miss you')
print(result)