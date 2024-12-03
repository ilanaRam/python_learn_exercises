def main():
    # we wish to remove 'all' acurances of element = 2
    
    # way 1: list comprehension
    my_list = [1,2,3,4,5,2,2]    
    my_list = [elem 
                for elem in my_list 
                    if elem != 2]
    print(f"By list comprehension: {my_list}")

    # way 2: use .remove(element) ability of a list
    my_list = [1,2,3,4,5,2,2]  
    elem_to_remove = 2
    cnt = my_list.count(elem_to_remove)
    for _ in range(cnt):
        my_list.remove(elem_to_remove)
    print(f"By removing all occurences: {my_list}")

    # way 3: use .pop(index) ability of a list
    my_list = [1,2,3,4,5,2,2]
    elem_to_remove = 2
    cnt = my_list.count(elem_to_remove)
    for _ in range(cnt):        
        my_list.pop(my_list.index(elem_to_remove))            
    print(f"By poping all occurences: {my_list}")       

    # way 4: del elem from a list from an index
    my_list = [7,3,4,5,2,2,2]    
    elem_to_remove = 2
    cnt = my_list.count(elem_to_remove)
    for _ in range(cnt): 
        del my_list[my_list.index(elem_to_remove)]            
    print(f"By del all occurences: {my_list}")

    # way 5: filter elem from a list from an index - same as map()
    my_list = [7,3,4,5,2,2,2]    
    elem_to_remove = 2
    my_list = list(filter(lambda x: x!=elem_to_remove, my_list)) 
    print(f"By filtering all occurences: {my_list}")

    
if __name__ == '__main__': 
    main()