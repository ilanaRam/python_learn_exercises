import os






def make_ping(host):
    command = None

    # command = f"ping -c 4 {host}" if os.name != 'nt' else f"ping -n 4 {host}"
    # 4 means make 4 pings
    if os.name == 'nt':
        # for OS = windows
        command = f"ping -n 4{host}"
    else:
        # for OS = linux
        command = f"ping -c 4 {host}"

    print(f"Command for pinging basing on OS is: {command}, os is: {os.name}")

    # Execute the command and get the output
    print(f"Sending the ping command at this moment")
    response = os.system(command)

    if response == 0:
        print(f"Res is {response}, Ping to {host} was successful!")
    else:
        print(f"Res is {response}, Ping to {host} failed.")



if __name__ == '__main__':
    host = "google.com"
    make_ping(host)
