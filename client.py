# Task 2: Making a web client
# Instead of using a browser, write your own HTTP client to test your server. 
# Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output.

#Kodeinspirasjon hentet fra https://www.techwithtim.net/tutorials/socket-programming/

import socket
import sys

# Setter HOST, PORT og FILE til å være user argument 0,1 og 2
# Jeg har valgt å ikke lage feilhåndtering for user input da det feilhåndteres på serversiden 
# og hvis det ikke kommer en melding tilbake får brukeren en feilmelding uansett.
HOST = sys.argv[1]
PORT = int(sys.argv[2])
FILE = sys.argv[3]
ADDR = (HOST, PORT)
FORMAT = "utf-8"
print(f"[INPUT] {ADDR, FILE}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definerer socket med socket familie og type


def recieve():
    try:
        sock.connect(ADDR)
        request = f"GET /{FILE} HTTP/1.1"
        request = request.encode(FORMAT)
        sock.send(request)
        print(sock.recv(99999).decode(FORMAT))
    except:
        print("[ERROR] Could not connect, please try again")

recieve()