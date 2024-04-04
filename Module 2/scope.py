# global variable
balance = 3000

def buy_things(item, price):
    # local variable scope
    # you can access globl variable without using the global keyword
    dream_phone ='xPhone'
    # if you want to modify a global variable, you have to use the global keyword
    global balance
    print('previous balance value', balance)
    balance = balance - price
    print(f'balance after buying {item}', balance) 
    print('Balance inside the function', balance)
    
buy_things('Sunglass', 1000)