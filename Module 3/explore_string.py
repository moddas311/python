name = 'Shakib\'s Khan' #scape
name_2 = "Shakib Khan"


# multi line of string
name_3 = """
    Shakib Khan 
    Number one
"""
print(name_2)

# string ia sequence of characters
for char in name_2:
    print(char)
    
print(name[2])
print(name[1:6])
print(name[-3])
print(name[::-1])

# mutable means changeable
# immutable means you can not change it

print(name)

if "Khan" in name:
    print("Exist")