numbers = [12, 56, 98, 78, 56, 12, 26, 98]
person_1 = ['Kala chan', 'Kalipur', 23, 'student']

# key value pair
# dictionary
# object
# overlap with set
# {key: value, key: value, key: value}

person = {'name': 'kailla', 'address': 'shibpur','age':23, 'job': 'student'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

# del person['age']
person['language'] = 'python'
person['name'] = 'BD' # Mutable value change kora jai
print(person)

for key, value in person.items():
    print(key, value)