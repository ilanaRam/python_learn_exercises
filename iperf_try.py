
# check iperf is installed on the ps
# use iperf

import subprocess # for sending command line commands
import time
import os
import multiprocessing
from multiprocessing import Process, Queue, Pipe
import psutil

def handle_iperf_process_is_running(process_name):
    print(f" checking if process {process_name} is running on this pc ...")

    for proc in psutil.process_iter():
        #print(f" Process {proc.name()}")
        if proc.name() == process_name:
            print(f" Process {proc.name()} is running, pid is {proc.pid}, {proc.exe()}, {proc.cwd()}, {proc.status()}  {proc.is_running()}")
            print(f"will be killed ..")
            try:
                proc.kill()
            except psutil.NoSuchProcess:
                print(f"No such process: {proc.pid}")
            except psutil.AccessDenied:
                print(f"Access denied to {proc.pid}")
    else:
        print(f"Process {process_name} was not running on this pc, test can started")

def run_iperf_server_process():
    print(f"Iperf Server starts running ....")
    path_to_iperf = "C:\\Program Files\\iperf3.17_64\\"
    command = [path_to_iperf + "iperf3.exe", "-s"]

    result = subprocess.run(command)

    #print(f"Server report is: {result}") # ----> Nothing is reported here


def run_iperf_client_process(num_of_transactions, my_quque):
    print(f"Iperf Client starts running ....")
    print('process id:', os.getpid(), '\n', '\n')


    # by default iperf sends TCP packets, in case we wish UDP we can indicate it by '-u'
    path_to_iperf = "C:\\Program Files\\iperf3.17_64\\"

    t = f"-t {num_of_transactions}" if num_of_transactions else ""

    command = [path_to_iperf + "iperf3.exe", "-c", "localhost", t, "-i", "1", "-V", "--forceflush"]  # 127.0.0.1, TCP by default "-t", "1"


    result = subprocess.Popen(command,stdout=subprocess.PIPE)

    for line in result.stdout:
        print("Client report: adding new line from iperf report --> queue ")
        my_quque.put(line.decode())

    print(f"Client is Done, checking to see if iperf server alive - if so will add msg into queue to kill iperf server")


def reporter_process(my_quque, stoping_msg):
    while True:
        if my_quque.empty():
            continue
        item = my_quque.get()
        print(f"Reporter task: {item}, stopping message: {stoping_msg}")
        if stoping_msg in item:
            print(f"Reporter task: Done")


if __name__ == "__main__":
    print("Number of cpus is : ", multiprocessing.cpu_count())
    my_quque = Queue()

    handle_iperf_process_is_running("iperf3.exe")

    reporter = Process(target=reporter_process,args=(my_quque,"iperf Done.",))
    reporter.start()

    # must be a process
    server = Process(target=run_iperf_server_process,args=())
    server.start()
    my_flag = True
    time.sleep(2)

    client = Process(target=run_iperf_client_process,args=(3, my_quque,))
    client.start()
    client.join()


    # rest of the processes we need to kill, because:
    # 1. server never stops listening
    # 2. reporting process never finishes read the Q
    # after Client has reported he is Done - I kill all other process

    #server.join()
    #reporter.join()
    if reporter.is_alive():
        reporter.terminate()
        reporter.kill()

    if server.is_alive():
        server.terminate()
        server.kill()

    print("All processes have finished")




