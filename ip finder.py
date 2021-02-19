import socket


def get_host_name_IP():
    try:
        host_name = socket.gethostname()
        host_IP = socket.gethostbyname(host_name)
        print("hostname: ", host_name)
        print("IP: ", host_IP)
    except:
        print("unable to get the host ip address")


get_host_name_IP()
