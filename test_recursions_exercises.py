from typing import List

def test_flatten_list_of_lists(my_list_of_lists: list) -> list:
    flaten_list = []
    print(f"The func is called with: {my_list_of_lists}")

    for item in my_list_of_lists:         
        if isinstance(item, List):
            print(f"The item is a list, we need recursion again ..")
            flaten_list.extend(test_flatten_list_of_lists(item))
        else:            
            flaten_list.append(item)
            print(f"The flatten list is: {flaten_list}")
    
    return list(flaten_list)
        

def test_flatten_nested_lists(my_list): 
    flatten_list = []
    print(f"The func is called with: {my_list}")
    
    # this for is instead of the stopping criteria !!
    for item in my_list:         
        print(f"The current item is: {item}")
        if isinstance(item, List):
            print(f"Only if the item is a list we need recursion again ..")  
            flatten_list.extend(test_flatten_nested_lists(item))            
        else: 
            flatten_list.append(item)
            print(f"The new flat list is now: {flatten_list}")
    
    print(f"This is what returned right now: {flatten_list}")
    return list(flatten_list) # each time the function wil finish the for loop this will be returned
                              # here we have 3 for loops:
                              # [3,4]
                              # [2,3,4,5] 
                              # [1, 2, 3, 4, 5, 6] 

# ---------------------------------------------------------
def fibonacci_list_recursion(n):
    # Base case for recursion
    if n == 0:
        return [0]  # The first Fibonacci number is [0]
    elif n == 1:
        return [0, 1]  # The first two Fibonacci numbers are [0, 1]
    
    # At  developement:  at the last time will be returned [0,1]
    fibs = fibonacci_list_recursion(n - 1)
    
    # At the closing: 
    next_fib = fibs[-1] + fibs[-2]  # Sum the last two Fibonacci numbers
    fibs.append(next_fib)  # Append the next Fibonacci number
    
    return fibs


# ---------------------------------------------------------
def fibo_gen(n):
    a,b = 0,1

    while n: 
        yield a
        tmp = a
        a = b
        b = tmp + b
        n -= 1        

def test_create_fibo_seria_with_generator(n):
    fibo_list = []
    gen = fibo_gen(n)

    for i in gen:
        fibo_list.append(i) 
    return fibo_list
# ---------------------------------------------------------
def make_factorial_with_recursion(n):
    print(f"The func is called with: {n}")
    if n == 1:    
        return 1   # also ok to put here n
    res = make_factorial_with_recursion(n-1) # up untill this line the function is laying out recursivelly , each call return 
    # starting from here - the next operations are executed when fuction calls are returned
    res = n * res
    
    return res

# ---------------------------------------------------------
def reverse_string(my_str, index=0):
    
    # stop criteria and operation to be done when stop criteria is matched 
    if len(my_str) == 0: 
        return my_str
    
    res = reverse_string(my_str[:-1]) # this is laying out of the func - recursive call to itself
    # here are the operations to be done when function is returned
    res = my_str[-1] + res

    return res  


def power_recursiv(base, po): 
    if po == 0:
        return 1
    elif po == 1:
        return base
    
    res = power_recursiv(base, po = po-1) #f(2,3), f(2,2), f(2,1)
    # first 1 will be returned 2
    res = res * base

    return res

# ---------------------------------------------------------
def sum_list_recursivelly(my_list): 
    print(f"called func with {my_list}")
    
    if len(my_list) == 0: # == if not my_list
        print(f"rec is endded, returned: {0}")
        return 0

    # laying out my function recursivelly
    print(f"func to be called with {my_list[:-1]}")
    
    # this is done on recursive calls of the func -----> 
    res = sum_list_recursivelly(my_list[:-1])    

    # this is done on the return only !!!  <-----
    res = my_list[-1] + res 
    return res # this is returned to prev func call state


if __name__ == '__main__':

    # my_list = [1,[2,[3,4],5],6]
    # flatten_list = test_flatten_nested_lists(my_list)
    # print(f"The flatten list is: {flatten_list}")

    my_list_of_lists = [[1,2], 
                        [3,4]]
    flatten_list = test_flatten_list_of_lists(my_list_of_lists)
    print(f"The flatten list is: {flatten_list}")

    # res = fibonacci_list_recursion(4)
    # print(F"The fibo list with recursion is: {res}")

    # res = test_create_fibo_seria_with_generator(6)
    # print(F"The fibo list with generator is: {res}")   

    # res = make_factorial_with_recursion(5) 
    # print(f"The factorial is: {res}")

    # res = reverse_string("kido")
    # print(f"The reversed string is: {res}")
    
    # res = power_recursiv(base = 3, po = 0)
    # print(f"The power_recursiv is: {res}")

    # res = sum_list_recursivelly([1,2,3,4])
    # print(f"The recursiv sum is: {res}")