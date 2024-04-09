class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            
    def withdraw(self, amout):
        if amout < self.min_withdraw:
            print (f'You can withdraw below {self.min_withdraw}')
        elif amout > self.max_withdraw:
            print(f'You can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amout
            print(f'Here is your money {amout}')
            print(f'After withdraw your balance is {self.get_balance()}')
        
        
brac_bank = Bank(20000)
brac_bank.withdraw(17000)

dbbl = Bank(5000)
dbbl.deposit(50000)
print(dbbl.get_balance())

        
    