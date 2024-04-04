numbers = [45, 87, 65, 43, 85, 90, 14, 26, 61, 70, 15]

odds = []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
            
print(odds)

# odds_num = [num for num in numbers if num % 2 == 1]
odds_num = [num for num in numbers if num % 2 == 1 if num % 5 == 0] 

print(odds_num)


players = ['Shakib', 'Musfik', 'Mustafiz']
ages = [30, 28, 32]

age_comb = []

for player in players:
    print('Player: ', player)
    for age in ages:
        print(player, age)
        age_comb.append([player, age])
print(age_comb)

age_comb_2 = [[player, age] for player in players for age in ages]

print(age_comb_2)