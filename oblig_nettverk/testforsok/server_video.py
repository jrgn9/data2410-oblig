# based on https://www.youtube.com/watch?v=3QiPPX-KeSc

import socket
import threading    # creating multiple threads in one program

# import pickle for å sende objekter

HEADER = 64 # A header that is sent first, telling us the length of the message
PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname()) # finds host ip automaticly
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Defines socket with socket family and type   
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Create a msg_length to recive HEADER telling us the length of the message
        # Decodes it with utf-8, and converts it to an int
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
        
            print(f"[{addr}] {msg}")    # Prints message
            conn.send("Msg received".encode(FORMAT))    # Sends message to client that message is recieved
    conn.close()    # Close connection when connected = False
        

# When new connection occurs, we pass that connection to handle_client
# we give it connection and address
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()    
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        

print("[STARTING] server is starting...")
start()