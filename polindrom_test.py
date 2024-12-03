from functools import reduce 



"""
How to check if POLINDROM, do: 
    1. revers the object (by: reduce | slicing)
    2. compare to original one

"""

def build_int_func(tmp_num, i):
    return tmp_num + int(i)



def convert_from_iterrable(item, desired_type):
    if isinstance(item, str) and desired_type == str:
        print(f"No need to convert back")
        return item
    
    elif isinstance(item, list) and desired_type == str:        
        item = "".join(str(i) for i in item) # join must receive iterable of string, else iterate its elements and cast each str(i)
        print(f"The reversed item: {item}")
        return item
    
    elif desired_type == int:               
        item = int("".join(item))   # join must receive iterable of string !!!
        print(f"The reversed item: {item}")
        return item
    else: 
        return item

# item can be of a types: 
# str
# list of strings
# list of ints
# int
def convert_to_iterrable(item): 
    
    if isinstance(item, int):        
        print("The item is 'int', will be converted to 'str'")
        item = str(item)       
        return item        
    else: 
        # str / list of ints / list of strings are iterables, so no need to convert
        print("Already itrable, no need to convert")
        return item

# this func result will be: list of strings -> ['','','','','']
def reverse_func(tmp_list, elem_from_itterable):
    return [elem_from_itterable] + tmp_list





def check_item_is_polindrom(original_item): 
    print(f"Will be checked this item: {original_item}")

    # 1. convert to iterable
    iterable_item = convert_to_iterrable(original_item)

    # 2. reverse 
    reversed_iterable_item = reduce(reverse_func, 
                                    iterable_item,  # my iterrable to reverse 
                                    [])             # initial empty iterable (to hold the reversed iterrable)    
    # 3. compare reversed vs original
    if original_item == convert_from_iterrable(reversed_iterable_item, desired_type=type(original_item)):
        print(f"The item is Polindrom\n")
    else:
        print(f"The item IS NOT Polindrom\n")




if __name__ == '__main__':     
    # str -----------------------    
    check_item_is_polindrom("abba")
    check_item_is_polindrom("arbba")
    
    # list of ints ---------------------  
    check_item_is_polindrom([1,2,3,2,1])
    check_item_is_polindrom([1,4,2,3,2,1])

    # list of strings -----------------  
    check_item_is_polindrom( ['1','4','4','1'])  
    check_item_is_polindrom(['1','4','2','3','2','1'])

    # number ------------------------  
    check_item_is_polindrom(12321)
    check_item_is_polindrom(122321)
