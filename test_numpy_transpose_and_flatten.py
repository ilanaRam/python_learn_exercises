import numpy as np
import sys

def numpy_try():
    my_array = np.array([[1,2,3],
                            [4,5,6]])
    print(f"Original array:{my_array}\n")
    
    print(f"Transposed array: {np.transpose(my_array)}\n")
    print(f"Flatten array: {np.ndarray.flatten(my_array)}\n")
    

    """ we will get this output: 
    * while original array is not changed, created new array
        [[1 4]
         [2 5]
         [3 6]]
    """

def get_user_metadata():
    lines = None
    items = None

    while True: 
        try: 
            my_in = input("please enter in this format: [num of lines] space separation [number of elements in line]:  ")
            if my_in in ('break', 'exit', 'bye', ''): # '' is ENTER
                print(f"User desided to finish")    
                return None, None
            
            lines, items = my_in.strip().split()
            print(f"lines: {lines}, items: {items}")

            if not lines.isnumeric() or not items.isnumeric():
                raise Exception("not numeric input, both or at least one of")
            
            lines = int(lines)
            items = int(items)
            if lines == 0 or lines < 0 or items == 0 or items < 0:
                raise Exception("invalide input, both or at least one of")   
            break        
        except Exception as ee: 
            print(f"Error: {ee}, invalide input, try again ...")
            continue       
        
    return lines, items  
         
def get_user_data(lines, items): 
    my_array = []
    i = lines

    while i:
        try: 
            curr_items = input(f"please enter items separated with space: ({items} per input, number of inputs will be {lines}) ")            
            if not curr_items: 
                raise Exception("Were received empty input")
            curr_items = curr_items.strip().split()  
            if len(curr_items) != items:
                raise Exception(f"Were received input with amount of items != than {items}")                          
            my_array.append(curr_items)
            i -= 1
        except Exception as ee: 
            print(f"The Error is: {ee}")
        finally: 
            continue
                 
    my_array = np.array(my_array)
    print(f"The array is:\n {my_array}")
    return my_array


if __name__ == '__main__': 
    
    lines, items = get_user_metadata()
    if not lines or not items:
        print(f"Not enough information about meta data")
        sys.exit()
    
    my_arr = get_user_data(lines, items)
    if my_arr is None: 
        print(f"The array is empty, nothing to work with !!!")
        sys.exit()
        
    trans_array = np.transpose(my_arr)
    print(f"Transposed array: {np.transpose(my_arr)}\n")
    print(f"Flatten array: {np.ndarray.flatten(my_arr)}\n")
    