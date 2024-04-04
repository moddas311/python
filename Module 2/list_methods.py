numbers = [12, 45, 98, 68]
numbers.append(99)
print(numbers)

numbers.insert(2, 55)
print(numbers)

if 99 in numbers:
    numbers.remove(99)
print(numbers)

if 100 in numbers:
    numbers.remove(100)
print(numbers)

last = numbers.pop()

print(last, numbers)

index = numbers.index(68)

if 68 in numbers:
    index = numbers.index(68)
    print(index)

shorted = numbers.sort()
print(numbers)


