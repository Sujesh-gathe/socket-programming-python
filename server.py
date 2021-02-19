import socket

# defining socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding the socket on a host
s.bind((socket.gethostname(), 1234))

# establishing connections
s.listen(5)

# building connections with client and server
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server!", "utf-8"))

    
