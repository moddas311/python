# list --> []
# tuple --> ()
# set --> {}

# set: unique items collection, no duplicate

numbers = [ 6, 12, 96, 96, 57, 67, 57, 98, 45, 12]
# print(numbers)

numbers_set = set(numbers)
print(numbers_set)

numbers_set.add(23)
print(numbers_set)

numbers_set.remove(98)
print(numbers_set)

# numbers_set[1] = 5 # eivabe man bosano jabe na 
# print(numbers_set)

for number in numbers_set:
    print(number)
    
if 9 in numbers_set:
    print('9 is exixt')
elif 23 in numbers_set:
    print('98 is exixt')
    
A = {1, 3, 5}
B ={1, 2, 3, 5, 7}
print(A & B) #A intersction B
print(A | B) #AUB