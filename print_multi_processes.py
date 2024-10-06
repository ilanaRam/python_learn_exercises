# importing the multiprocessing module
import time
from queue import Queue

from multiprocessing import Process, Queue, Lock
import os

def print_cube(num_of_transactions, my_queue, my_lock):
    """
    function to print cube of given num
    """
    while num_of_transactions:
        with my_lock:
            print(f"Process print_cube, id: {os.getpid()}, printing: {num_of_transactions}")
            my_queue.put(f"Process print_cube, id: {os.getpid()}, printing: {num_of_transactions}")
        num_of_transactions -= 1
        time.sleep(5)


def print_square(num_of_transactions, my_queue, my_lock):
    """
    function to print square of given num
    """
    while num_of_transactions:
        with my_lock:
            print(f"Process print_square, id: {os.getpid()}, printing: {num_of_transactions }")
            my_queue.put(f"Process print_square, id: {os.getpid()}, printing: {num_of_transactions}")
        num_of_transactions -= 1
        time.sleep(1)


if __name__ == "__main__":
    my_queue = Queue()
    my_lock = Lock()
    num_of_transactions = 100

    print(f"I am the main process: {os.getpid()}, going to spawn 2 more sub processes ")
    print("\n1.creating / initiating of the processes ...")
    print_square_p = Process(target=print_square,                           # function to be run by a process
                             args=(num_of_transactions, my_queue, my_lock)  # argument to the function delivered as a tuple
                                            )
    print_cube_p = Process(target=print_cube,
                           args=(num_of_transactions, my_queue, my_lock))

    print("\n2.starting the process - print_square_p")
    print_square_p.start()
    print("\nstarting the process - print_cube_p")
    print_cube_p.start()

    print("\n3.wait until process - print_square_p is finished")
    print_square_p.join()
    print("\nwait until process - print_cube_p is finished")
    print_cube_p.join()

    print("\nCheck if processes are alive ...")
    print("Process print_square_p is alive: {}".format(print_square_p.is_alive()))
    print("Process print_cube_p is alive: {}".format(print_cube_p.is_alive()))

    print("\nwe are here - because both processes are Done !!")
    print("Done!")