import numpy as np


def float_and_revert():
    my_list = [1,2,3,4,-8,-10]
    np_arr = np.array(my_list,float)

    print(f"Way1 - Reverting np array, slicing: ")
    my_new_np_arr = np_arr[::-1]
    print(f"the new np reversed array is: {my_new_np_arr} ")

    print(f"Way2 - Reverting np array: np.flip")
    my_new_np_arr = np.flip(np_arr)
    print(f"the new np reversed array is: {my_new_np_arr} ")

if __name__ == '__main__':
    float_and_revert()

    