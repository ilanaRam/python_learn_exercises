from functools import reduce

"""
It is all about giving weight for each cases
# lower weight to most important cases 
# higher weight to less important cases 

in this exercise i had the next rules: 
1. lowercase letters > uppercase letters
2. odd digits > even digits

and I had one more rule: (this rule connects between 1 and 2): 
3. uppercase letters > digits (either it odd / even digit)

so the weight are:
    lower case letters -> 1
    upper case letters -> 2
    odd digits         -> 3
    even digits        -> 4

    that is it !!
"""

def sort_strings(character):     
# lower case is first then upper case 
    if character.isalpha() and character.islower(): 
        print(f"{character}: ->1")
        return(1, character) 
    elif character.isalpha() and character.isupper():
        print(f"{character}: ->2")
        return(2, character)

    # if the character is str but it is a digit - so here we have to dort this way: odd digit is first then even digit 
    if character.isnumeric() and int(character) % 2 != 0:
        print(f"{character}: ->3")
        return(3, character) 
    elif character.isnumeric() and int(character) % 2 == 0:
        print(f"{character}: ->4") 
        return (4, character) 
    
      
def make_sort_string(orig_item):        
    my_new_seq = sorted(orig_item,key=sort_strings)
    my_sorted_item = "".join(my_new_seq)
    return my_sorted_item
    

def make_sort_list(my_list):    
    # way1:
    my_sorted_list = sorted(my_list)
    print(f"The sorted list is: {my_sorted_list}")

    # way2:
    # !!! my_list.sort() does not return a thing it sorts the list in place !! 
    # we directly can use my_list
    my_list.sort()
    print(f"The sorted list is: {my_list}")
    return my_list
    


if __name__ == '__main__': 

    # my_str = input("please enter string: ")
    # print(f"The orig str is: {my_str}")
    sorted_str = make_sort_string("Sorting1234")
    print(f"The sorted str is: {sorted_str}")

    sorted_item = make_sort_list([1,2,5,2,5,4,7])
    print(f"The sorted str is: {sorted_item}")



