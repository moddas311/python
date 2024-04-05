def multiple():
    return 3, 4
# print(multiple())

things = 'Pen', 'tripod', 'water bottle', 'phone', 'Laptop', 'football'

# print(type(things))

# print(things)
# print(things[0])
# print(things[-1])

# print(things[0:4])

if 'phone' in things:
    print('Exist')

for item in things:
    print(item)
    
# things[0] = 'Wow'

print(len(things))

# ignore
mega = ([2, 3, 4], [6, 8, 9, 5])
print(type(mega))
print(mega[0])
mega[0][1] = 33
print(mega)