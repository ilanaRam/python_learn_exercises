
def lef_rotate(my_array, steps_num):
    if not isinstance(steps_num, int):
        print(f"steps is not numeric, nop")
        return
    if not my_array or len(my_array) == 0:
        print(f"The array is empty")
        return
    if steps_num == len(my_array):
        print(f"number of left rotations = array size, nop")
        return
    if steps_num == 0:
        print(f"number of left rotations is 0, no need to rotate left")
        return
    if steps_num < 0:
        print(f"number of left rotations is negative, nop")
        return
    if not isinstance(steps_num, int):
        print(f"steps is not numeric, nop")
        return

    # 1. insert into first index last element
    # 2. delete last elem

    for i in range(steps_num):
        # insert last to the beginning
        my_array.insert(0,*my_array[-1:]) # also possible: my_array[-1] it gives element

        # delete last
        del(my_array[-1])
        # also possible:
        # my_array.pop()                # will remove last element from a list
        # my_array.pop(len(my_array)-1) # will remove element from specific index
        print(my_array)


if __name__ == '__main__':
    left_rotate_array = [1,2,3,4,5]
    lef_rotate(left_rotate_array, 2)
    # lef_rotate(left_rotate_array, 2)
    # lef_rotate(left_rotate_array, 3)
    # lef_rotate(left_rotate_array, 4)
    # lef_rotate(left_rotate_array, 5)