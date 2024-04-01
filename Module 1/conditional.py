# in, not, not in, is, not is
# and or

a = 2

if a > 7:
    print('5 er beshi')
elif a > 3:
    print('3-5 er majhamajhi') 
elif a == 2:
    print('2 er soman soman')
else:
    print('7 er kom')
    
boss = False

if boss is not True:
    print('Lunch er por asen')
else:
    print('Boss khaite geche')
    
# Nested conditions
coin = 'head'

if boss == True:
    print('Boss are joss')
    if coin == 'head':
       print('Batting')
    else:
        print('bowling')
else:
    print('You are loss')