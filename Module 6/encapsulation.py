# encapsulation --> hide details
# access modifier: public, private, protected 

class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public attribute 
        self._branch = 'Farmgate' # protected attribute 
        self.__balance = initial_deposit # private attribute 
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f'You haven\'t enough balance you have only: {self.__balance}'
    
    def get_balance(self):
        return self.__balance 
        

moddasir = Bank('Moddasir', 500)
moddasir.deposit(500)
# moddasir.withdraw(200)

print(moddasir.withdraw(200))
print(moddasir.get_balance())
