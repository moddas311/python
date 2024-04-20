num = []
for i in range(1, 11):
    num.append(i)
# print(num)

# list compression
""" 
new_list = [[i, i ** 2] for i in range(1, 11)] 
print(new_list) 
"""

# tuple 
""" 
new_list = [(i, i ** 2) for i in range(1, 11) if i % 2 == 1 if i ** 2 <= 50] 
print(new_list) 
"""

num = []

for i in range(3):
    for j in range(3):
        num.append([i, j])
print(num)


#list compression
new_list = [[i, j] for i in range(3) for j in range(3)]
print(new_list)