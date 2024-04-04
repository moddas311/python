from function import double_it # simple vabe use kora onno file theke 
from kargs_multiple import full_name as name # ekta folder theke amra rename koreo function gula use korte pari
from default_args import * # default args file theke sob import hbe 

money = input('Give me money i will make it double: ')
money_int = int(money)
result = double_it(money_int)
print('That''s your money i make it double:', result)

f_name = name('Khadija', 'Hamida')
print(f_name)