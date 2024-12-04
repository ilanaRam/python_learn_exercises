"""
in this excersize I will work with apis of the collection deque
append, appendleft, pop, popleft on the deque d
"""

from collections import deque

APPEND = 'append'
APPEND_LEFT = 'appendleft'
POP = 'pop'
POP_LEFT = 'popleft'

def get_input_amount_of_commands():       
    while True:        
        num_input = input("Please enter number of commands: ")
        try: 
            if not num_input: 
                break # if user asks to finish
        
            if not num_input.isnumeric():
                raise Exception
            
            num_input = int(num_input)
            if num_input == 0 or num_input < 0:
                print(f"The input is 0 or less, try again ...")
                continue
            return num_input
        except Exception as ee: 
            print(f"Error input: {ee}, try again ...")


def build_deque(number_of_commands): 
    my_deque = deque()
    
    print(f"Please enter {number_of_commands} commands, format is: <cmd> <number>")
    
    while number_of_commands:  
        try:                 
            cmd = input("Please enter command: ").strip()
            print(f"{cmd}")   

            if not cmd:                 
                print(f"User asked to finish the input ...")
                break # finish        
            if (cmd == POP and len(my_deque) == 0) or (cmd == POP_LEFT and len(my_deque) == 0):
                raise Exception("The deque is empty, yet has items to pop")
            elif cmd == POP:
                my_deque.pop()
                print(f"Poped a number from decue: {number}: {my_deque}")
            elif cmd == POP_LEFT:
                my_deque.popleft()
                print(f"Poped a number from decue: {number}: {my_deque}")
            else: 
                if ' ' not in cmd: 
                    raise Exception(f"Received incorrect command: {cmd}, please retry")
                
                cmd, number = cmd.split()
                if not number.isnumeric(): 
                    raise Exception(f"Received incorrect command: {cmd},{number}, please retry")
                number = int(number)

                if cmd not in [APPEND, APPEND_LEFT]: 
                    raise Exception(f"Received incorrect command: {cmd}, please retry")                    
                
                if cmd == APPEND: 
                    my_deque.append(number)
                    print(f"Added a number to decue: {number}: {my_deque}")            
                elif cmd == APPEND_LEFT: 
                    my_deque.appendleft(number)  
                    print(f"Added a number to decue: {number}: {my_deque}")
                
                number_of_commands -= 1    
        except Exception as ee: 
            print(f"Error: {ee}, keep trying ...")
    
    if len(my_deque) == 0: 
            print(f"The deque is empty")
    else:
        print(f"The deque is: {my_deque}")
    
    
    




if __name__ == '__main__': 
    amout_of_input = get_input_amount_of_commands()
    build_deque(amout_of_input)
