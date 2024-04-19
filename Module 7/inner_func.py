# function is a first class object

def double_decker():
    print('Starting the double decker!')
    def inner_func():
        print('Inside the inner')
        return 100
    return inner_func

# print(double_decker())    
print(double_decker()())    
    
    
def do_something(work):
    print('Work started')
    # print(work)
    work()
    print('work ended')

# do_something(2)
# do_something('I am busy')

def coding():
    print('started coding with python')

# do_something(coding)

def sleeping():
    print('Just wow weather so start sleeping')
do_something(sleeping)