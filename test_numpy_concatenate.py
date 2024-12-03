import numpy as np
import sys

def concat_np_arrays_by_axis(): 
    array_1 = np.array([[1,2,3],[0,0,0]])
    array_2 = np.array([[0,0,0],[7,8,9]])    

    print(f"The new aray is: {np.concatenate((array_1, array_2), axis=0)}") 
    """
        [[1 2 3]
        [0 0 0]
        [0 0 0]
        [7 8 9]
    """
    print(f"The new aray is: {np.concatenate((array_1, array_2), axis=1)}")
    """
        [[1 2 3 0 0 0]
        [0 0 0 7 8 9]]
    """


def get_meta_data():
    pass

def get_arrays_elems(n, m, p):
    pass

def concatinate_arrays(ar_1, ar_2, axis = 0):
    pass



if __name__ == '__main__':
    concat_np_arrays_by_axis()
    
    n,m,p = get_meta_data()

    if not n or not m or not p:
        print(f"Not enough information about meta data")
        sys.exit()
    
    ar_1, ar_2 = get_arrays_elems(n,m,p)
    if ar_1 is None or ar_2 is None: 
        print(f"The array/s is/are empty, nothing to work with !!!")
        sys.exit()

    arr = concatinate_arrays(ar_1, ar_2)
    print(f"The new aray is: {arr}")

    arr = concatinate_arrays(ar_1, ar_2, 1)
    print(f"The new aray is: {arr}")

