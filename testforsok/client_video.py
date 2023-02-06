# based on https://www.youtube.com/watch?v=3QiPPX-KeSc

import socket

HEADER = 64 # A header that is sent first, telling us the length of the message
PORT = 9999
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # Lager først en header som sender lengden av message
    # Padder meldingen så den skal bestå av 64 bytes (definert av server)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))   # Padding that adds empty bytes for HEADER length minus length of send
    client.send(send_length)
    # Sender selve meldingen etter HEADER
    client.send(message)
    print(client.recv(2048).decode(FORMAT))    # Printer melding sendt fra server (2048 er byte grensa for mottak)

#Meldingene vi sender til server
send("HAAALLLOOOOOO??????")
input() # Gjør at man må trykke enter i terminal for å sende neste melding
send("HJELP")
input()
send("JEG VIL UUUUT")
send(DISCONNECT_MESSAGE)