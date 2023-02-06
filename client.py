# Task 2: Making a web client
# Instead of using a browser, write your own HTTP client to test your server. 
# Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output.

import socket
import sys

# Setter HOST, PORT og FILE til å være user argument 0,1 og 2
HOST = sys.argv[1]
PORT = int(sys.argv[2]) # Burde kanskje hatt error handling for PORT, men lot være i denne oppgaven.
FILE = sys.argv[3]
ADDR = (HOST, PORT)
FORMAT = "utf-8"
print(ADDR, FILE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definerer socket med socket familie og type


#print("[ERROR] Could not connect")

def recieve():
    try:
        sock.connect(ADDR)
        request = f"GET /{FILE} HTTP/1.1"
        request = request.encode(FORMAT)
        sock.send(request)
        print(sock.recv(99999).decode(FORMAT))
    except:
        pass

recieve()