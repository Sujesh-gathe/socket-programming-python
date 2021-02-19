import socket

# defining socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to server
s.connect((socket.gethostname(), 1234))

# recving msg from server in 2^10 byte
msg = s.recv(1024)
print(msg.decode("utf-8"))


