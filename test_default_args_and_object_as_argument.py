
class Car: 
    def __init__(self) -> None:
        self.color = None   


# pay attension this 'extern to class function can assecc to all fields of the delivered object - it is not like in any other language
def change_given_object_to_given_color(vehicle, new_color="Blue"):    
        
    print(f"car before setting colores: {Car().color}")
    vehicle.color = new_color
    print(f"car after setting colores: {Car().color}")


def object_as_argument_to_func():           
    change_given_object_to_given_color(Car(), "Red") 
    change_given_object_to_given_color(Car())   
# --------------------------------------------------------------------------------#

def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower()

# func greeting receives func as argument (any func)
# such func is called: higher-order functions (function that gets another func as agument)
def greet(func): 
    
    # storing the function in a variable    
    #  greeting is a variable
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)

def function_as_argument_to_func():
    # here we call a function greet() with input argument -> another function
    greet(shout)
    greet(whisper)

def main():
    function_as_argument_to_func()
    object_as_argument_to_func()
    
    
    
   

if __name__ == '__main__':
    main()




