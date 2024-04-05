# lamda

# def doubled(x):
#     return x*2

doubled = lambda num: num*2
squred = lambda num: num**2
result = doubled(44)
output = squred(9)
# print(result, output)


add = lambda x, y: x+y 
sum = add(11, 66)
# print(sum)


numbers = [12, 56, 98, 78, 56, 12, 26, 98]
# doubled_nums = map(doubled, numbers)
doubled_nums = map(lambda x: x*2, numbers)
squred_nums = map(lambda x: x**2, numbers)
print(numbers)
print(list(doubled_nums))
print(list(squred_nums))

actors = [
    {'name': 'shabana', 'age': 55},
    {'name': 'sabnoor', 'age': 39},
    {'name': 'sabila noor', 'age': 29},
    {'name': 'srabonti', 'age': 40},
    {'name': 'shawon', 'age': 47}
]

junior = filter(lambda actor: actor['age'] < 40, actors)
fivers = filter(lambda actor: actor['age'] % 5 == 0, actors)

print(list(fivers))
print(list(junior))