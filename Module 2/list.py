# list, array, collection are same(simple terms)

numbers = [12, 45, 76, 99, 71, 33, 55, 89, 87, 92, 65]

print(numbers[3], numbers[-10])

# list(start: end) # start from the start index and stops before the end index 
print(numbers [2:6])
print(numbers [0:6])

# list(start: end: step)
print(numbers[2:6:1])
print(numbers[2:6:2])

print(numbers[7: 2: -1])
print(numbers[7: 2: -2])

print(numbers[:]) # print the all element in array 
print(numbers[4:]) # it will print from 4th number index to last 
print(numbers[:4]) # it will print 0 to 3rd index in the list
print(numbers[::-1]) # it will reverse the the array and it's a shortcut method 