# Calculator class to do add, deduct, multiply, divide

class Calculator:
    brand = 'Casio MS990'
    
    def add(self, num1, num2):
        sum = num1 + num2
        return sum
    
    def deduct(self, num1, num2):
        mainas = num1 - num2
        return mainas
    
    def multiply(self, num1, num2):
        gun = num1 * num2
        return gun
    
    def devide(self, num1, num2):
        bhag = num1 / num2
        return bhag
    
    
my_calculation = Calculator()

add = my_calculation.add(10, 10)
print(add)

biyog = my_calculation.deduct(10, 20)
print(biyog)

into = my_calculation.multiply(10, 20)
print(into)

bhag = my_calculation.devide(10, 20)
print(bhag)