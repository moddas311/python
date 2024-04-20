# lis mane hocche array
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[-1]) # negative index diyeo list access kora jai.

# new_list = numbers[0:4] # list slice kore felbe.
# new_list = numbers[2:] # list er 2 no. index theke baki index diye dibe.
# new_list = numbers[:4] # list er 0 index theke 4 index er ag porjonto dibe.
# new_list = numbers[0:5:3] # numbers[start: end: step]
# new_list = numbers[::-1] # reverse hoye jabe list
new_list = numbers[3: 0: -1]
print(new_list)