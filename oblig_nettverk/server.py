# Task 1: Making a simple webserver that handles one HTTP request at a time. 
# Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, 
# create an HTTP response message consisting of the requested file preceded by header lines, 
# and then send the response directly to the client.

import socket

# Final/static variabler
PORT = 9999 # Setter port
HOST = socket.gethostbyname(socket.gethostbyname(socket.gethostname()))   # Finner host ip automatisk
ADDR = (HOST, PORT) # Kaller host og port for ADDR (for å forenkle videre)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definerer socket med socket familie og type
sock.bind(ADDR) # binder adressen til socketen
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Hva gjør denne???

#Funksjon for å starte serveren
def start():
    sock.listen()   # Socket lytter etter connections
    print(f"[LISTENING] Server listening on {ADDR} \n") # Melding som viser host adresse som lyttes til

    connected = True
    while connected: # Kjører så lenge det er en connection
        conn, addr = sock.accept()    # Aksepter connection på adressen som kommer inn
        request = conn.recv(1024).decode()  # Tar imot request på 1024 bytes
        print(f"[REQUEST] {request}")   # Printer ut requesten til serveren

        # FEILHÅNDTERING:
        try:    # Prøver å åpne html-filen
            # Åpne html fil
            file = open("index.html", "r")  # HVA GJØR r???

        except FileNotFoundError: # Hvis filen ikke lar seg åpnes/ikke finnes
            # Sender feilmelding, lager 404 responsmelding og lukker connection
            fail_msg = "[ERROR] 404 Not Found"
            fail_msg = fail_msg.encode()
            conn.send(fail_msg)
            print("[CONNECTION CLOSED] Error 404 Not Found")
            response = "HTTP/1.1 404 Not Found\n"
            response = response.encode()
            conn.close()
            connected = False

        else:   # Hvis filen kan åpnes
            #leser html fil
            content = file.read()
            file.close()

            # Lager responsmelding
            response = "HTTP/1.1 200 OK\n"
            response += "Content-Type: text/html\n"
            response += "Content-Length: {}\n".format(len(content))
            response += "\n"
            response += content
            response = response.encode()

            #Sender responsmelding og lukker connection
            conn.send(response)
            print(f"[RESPONSE SENT] {response}")
            print("[CONNECTION CLOSED]")
            conn.close()
            connected = False

# Starter serveren
print("[STARTING] Server is starting")  # Melding om at serveren starter
start() # Kaller på funksjonen til å starte serveren