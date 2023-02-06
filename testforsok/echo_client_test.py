# Test av server, hentet fra https://realpython.com/python-sockets/

import socket

HOST = "127.0.0.1" # The server's hostname or IP address
PORT = 9999 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b"Hallooooo????")
    data = s.recv(1024)

print(f"recieved {data!r}")

# In comparison to the server, the client is pretty simple. It creates a socket object, 
# uses .connect() to connect to the server and calls s.sendall() to send its message. 
# Lastly, it calls s.recv() to read the server’s reply and then prints it.