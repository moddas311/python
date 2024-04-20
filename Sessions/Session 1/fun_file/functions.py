# function can return multiple value
def func(a, b):
    return a, b

# we can use default peramiter in function
def func(a, b, c = 10): # here c is a default or optional peramiter
    return a + b + c  

# when we don't know about the value or how many peramiter we should use then we need use *args in function 
def arg_func(name, *args):
    sum = 0
    for i in args:
        sum += i
    return name, sum

""" 
result = arg_func('Tamim',10, 15, 18, 19)
print(arg_func)
print(result[0]) # Here we will get the name  
"""

def square(x):
    return x ** 2

# Scope 
amount = 100
def fun_amount(name, *args):
    global amount # jodi global er man function er moddhe change korte chai taile age eivabe global kore nite hbe.
    amount = 500 # ekhon global amount er man o 500 hoye jabe 
    print(amount)
    
fun_amount('Assd')
print(amount)