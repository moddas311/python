def full_name(first, last):
    name = f'full name is: {first} {last}'
    return name

# take paremeter in order(serial wise)
# name = full_name('Moddasir', 'Mohaammad')
name = full_name(last='Rashed IBNE', first='Moddasir')
print(name) 



# def famus (**kargs)

def famous_name(first, last, **addition):
    name = f'{first} {last}'
    # print(adition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first= 'Taher', last='Ali', title= 'Hujur', title2='Syikh', last2='Trap')
print(name) 


# def function_name(num1, num2, *args, **kargs)
def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    return sum, mult, remain

everything = a_lot(55, 21)
print(everything)