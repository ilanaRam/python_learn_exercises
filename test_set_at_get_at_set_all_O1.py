order = 0

set_all_list = []      # [(obj, order)]
set_at_index_list = [] # [(obj, index, order)]

my_list = [0,0,0,0,0]

def set_at(index, obj):
    global order
    
    my_list[index] = obj
    order +=1
    set_at_index_list.append((obj, index, order))

def get_from(index):
    # get last from both dbs and decide upon the most updated
    if not set_all_list:
        return my_list[index]
    else: 
        if set_at_index_list[-1][-1] > set_all_list[-1][-1]:
            return my_list[index]
        else: 
            return set_all_list[-1][0]

def set_all(obj):
    global order

    order +=1
    set_all_list.append((obj, order))

def main():
    set_at(index=0,obj=1)
    print(f"set obj {1} into index {0}")
    
    set_at(index=1,obj=2)
    print(f"set obj {2} into index {1}")

    obj = get_from(1)
    print(f"got obj {obj} from index {1}")

    set_all(obj=8)
    print(f"set all indexes with  {8}")

    obj = get_from(index=1)
    print(f"got obj {obj} from index {1}")
    
    obj = get_from(index=0)
    print(f"got obj {obj} from index {0}")

if __name__ == '__main__':
    main()