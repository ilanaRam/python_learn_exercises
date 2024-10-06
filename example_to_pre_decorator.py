import re


# this is what we call DECORATOR
# called as third
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # this is a WRAPPER
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1 # here is called function inner1


# defining a function - we interested to decorate (to wrap) this function
def function_to_decorate():
    print("Hi I am the function to be called and decorated")

# called as first
# passing 'function_to_be_used' inside the decorator to control its behaviour.
# Decorator returns the same function but decorated
function_to_be_used = hello_decorator(function_to_decorate)

# decorated function - therefore will not be called as first func
# called as second
function_to_decorate()



