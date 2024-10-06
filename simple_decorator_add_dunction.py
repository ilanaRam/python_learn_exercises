
# ----------------------------------------------------
# example_1: without parameter to function, without decorator
# def print_hi():
#     print(f"Hi I am print_hi() function ")
#
# my_var = print_hi
#
# my_var()
# ----------------------------------------------------


# ----------------------------------------------------
# example_2: with decorator and wrapper
def decorator_for_add(func):
    # inner function that can be called and returned
    def my_wrapper():
        print(f"[WRAPPER] is called to run")
        res = func()
        print(f"[WRAPPER] is finished to run, the res is {res}")
    # here I call inner func and return its result
    return my_wrapper

def print_hi():
    print(f"Hi I am print_hi() function ")
    return "kuku"


# 1. assign a function to a variable (assign without () as we dont want to execute a function but only assign it)
# 2. decorate a function (that will wrapp it internally )
res_func = decorator_for_add(print_hi)

# 3. access the function from the variable - here will be called a decorator that will run the wrapper that wraps the function and call it from it
#res_func()


# ----------------------------------------------------
# example_3: with real decorator and annotations
from datetime import datetime

def log_datetime(func):
    '''Log the date and time of a function'''
    def wrapper():
        func()
    return wrapper


@log_datetime
def daily_backup():
    print(f'Daily backup is Started at: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')

#daily_backup()

# -------------------------------------------------
# example_4: real decorator with parameters
from datetime import datetime

def log_datetime(func):
    '''Log the date and time of a function'''
    def wrapper(*args, **kwargs):

        print(f"the numbers to be added are: {args[0]}, {args[1]}")
        res = func(*args) # also possible to call with: args[0], {args[1])
        print(f"the res is: {res}")

    return wrapper


@log_datetime
def add(x,y):
    res = x+y
    return res

# call to original (but decorated) func, will be called a decorator that will call orig func
add(10,20)