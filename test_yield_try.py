
# Exp1_ yield finitive amount of items without return
def count_up_to_generator(n):
    count = 1
    while count <= n:
        yield count
        count += 1

def try_finitive_generator(): 
    # In this example, count_up_to(5) is a function 
    # when we add 'yield' to a function - we make it to be a genrator func that will generat something each time we apply it
    # yeild returns generated value - each time we call the func. One value at the time - not all the values it is supposed to generate 

    # Here we create a generator that yields numbers from 1 to 5. 
    # The function doesn't return 'all' the numbers at once, it yields one number at a time. 
    # This is more 'memory-efficient' than returning a list with all values, especially for large ranges !!

    gen = count_up_to_generator(5)
    # using generator - each call to num will assign to a num the up to dated value of count
    for num in gen:
        print(num)
# --------------------------------------------------------

# Exp2_ yield infinitive amount of items without return
def count_up_to_infinit_generator():
    count = 1
    while True:
        print(f"generator() before yield , the counter is: {count}")
        yield count # at first call to gen will be perform gen func from the beginning till yield 
        count += 1  # at each next call to gen, will be called from yield line and till end of generator
        print(f"generator() after yield , the counter is: {count}")

def try_infinitive_generator():
    # here our generator - planned to generate infinitive amount of integers 
    # but we will apply it only 10 times - we will get only 10 integers 
    # each time we will get 1 integer only - generated at the moment we apply the generator func
    gen = count_up_to_infinit_generator()
    
    # call 1
    print(f"func()1 before call gen1")
    res = next(gen) # next(gen) - Each time you call the next() method on the generator object, it returns the next item.
    print(f"func()1, after call gen1,  counter is: {res}\n\n")
    
    # call 2
    print(f"func()2 before call gen2")
    res = next(gen) # next(gen) - Each time you call the next() method on the generator object, it returns the next item.
    print(f"func()2, after call gen2,  counter is: {res}")

# --------------------------------------------------------

# Exp3_ yield finitive amount of items with return - this way the caller side can know the generated ended !!
def return_generator():
    yield 1
    yield 2
    return "Done"  # This will cause StopIteration with the value "Done". Done is the last thing that will be returned

def try_return_generator(): 
    gen = return_generator()
    
    for _ in range(2):
        print(next(gen))
    # This will be the third time we call generator - this time generator ends and will return Done
    try:
        res = next(gen)        
    except StopIteration as ee:
        print(f"The generator ended hence will be resulted in exception whereI print the last yeilded value: {ee}")
# --------------------------------------------------------

def send_generator():   
    while True:
        received = yield  # yield here returns None , here it brings inside a value from outside
        print(f"gen(), Received: {received}")

def try_send_to_generator():
    gen = send_generator() # creation of the generator function
    print(f"func(), going to call next(gen)")
    res = next(gen)        # Start the generator (it reaches the first yield, actually gen func finishes with line received = yield )
    print(f"func(), res = {res}, expected to get None\n")
    
    print(f"func(), going to call gen.send(Hello)")
    gen.send("Hello")      
    
    print(f"\nfunc(), going to call gen.send(World)")
    gen.send("World")     
 # --------------------------------------------------------   

def multi_val_generator(): 
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def try_multiple_values_generator():
    gen = multi_val_generator() # generator creation, I need to know how many times to call the gen else I will get 'StopIteration' Exception 

    for num in gen: # under the hood for loop calls next(gen)
        print(num)
    res = next(gen) # if we call gen 1 more time, it has no more yields to supply, will be generated 'StopIteration' Exception
    print(f"the res is {res}")
# --------------------------------------------------------

# generator of the fibonachi seria of n items (it is always starts with 0,1)
# say n = 5: [0,1,1,2,3]
# say n = 10: [0,1,1,2,3,5,8,13,21,34]
def fibonachi_gen(n):
    a,b = 0,1
    for num in range(n): 
        yield a
        a = b
        b = a+b

def fibonachi_with_yield():
    # 2 elements in seria
    print("fibonachi seria with 2 items")
    gen = fibonachi_gen(2) 
    for num in gen: 
        print(num)  
    
    print("\nfibonachi seria with 5 items") 
    gen = fibonachi_gen(5)    
    for num in gen: 
        print(num)
    
    print("\nfibonachi seria with 10 items")
    gen = fibonachi_gen(10) 
    for num in gen: 
        print(num)
    

def read_files_gen(file_name):
    with open(file_name,'r') as file_desc:        
        
        for line in file_desc:
            yield line.lstrip() # Remove the 'newline' character


def reading_large_files_with_yield():
    file_to_read = "count_triplets.py"
    
    # create generator that will read line by line per request (not all lines at one time)
    gen = read_files_gen(file_to_read) 

    for line in gen: 
        print(line) # this is a request to read next line
    


if __name__ == '__main__':
    # try_finitive_generator()
    # try_infinitive_generator() # here I actually explained and showed what really happence which yield !!
    # try_return_generator()
    # try_send_to_generator()
    # try_multiple_values_generator()
    # fibonachi_with_yield()
    reading_large_files_with_yield()

