
def sum(a, b, c=0, d=0): #default parameter
    total = a+b+c+d
    return total

total = sum(10, 20)
print('total:', total) 


def all(*args):
    print(args)
    
    sum = 0
    
    for arg in args:
        sum += arg
    return sum

total_args = all(10, 20, 30, 80, 90)
print(total_args)