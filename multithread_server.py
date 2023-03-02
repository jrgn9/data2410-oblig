# Task 3: Making a multi-threaded web server
# Currently, your web server handles only one HTTP request at a time. 
# You should implement a multithreaded server that is capable of serving multiple requests simultaneously

#Kodeinspirasjon hentet fra https://www.techwithtim.net/tutorials/socket-programming/

#Imports av socket, multi threading og time (for sleep)
import socket
import threading
import time

# Final/static variabler
PORT = 9999 # Setter port
HOST = socket.gethostbyname(socket.gethostbyname(socket.gethostname()))   # Finner host ip automatisk
ADDR = (HOST, PORT) # Kaller host og port for ADDR (for å forenkle videre)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definerer socket med socket familie og type
sock.bind(ADDR) # binder adressen til socketen
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Setter socket options som gjør at bind kan reuse adresse


def handle_client(conn, addr):  # Funksjon for å håndtere en connection
    print(f"[CONNECTION] {addr} connected") # Printer adressen til connection

    connected = True
    while connected: # Kjører så lenge det er en connection
        request = conn.recv(1024).decode()  # Tar imot request på 1024 bytes
        print(f"[REQUEST] {request}")   # Printer ut requesten til serveren

        # FEILHÅNDTERING:
        try:    # Prøver å åpne html-filen
            # Åpne html fil
            file = open("index.html", "r")  # åpner filen med r (read)

        except FileNotFoundError: # Hvis filen ikke lar seg åpnes/ikke finnes
            # Lager 404 responsmelding, sender den og lukker connection
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

            # Lager suksessmelding med innholdet
            response = "HTTP/1.1 200 OK\n"
            response += "Content-Type: text/html\n"
            response += "Content-Length: {}\n".format(len(content))
            response += "\n"
            response += content
            response = response.encode()

            #Sender suksessmelding, innholdet og lukker connection
            conn.send(response)
            print(f"[RESPONSE SENT] {response}")
            time.sleep(20000)   # Lagt inn denne for å se at man kan koble til flere klienter før de disconnecter
            print("[CONNECTION CLOSED]")
            conn.close()
            connected = False


#Funksjon for å starte serveren
def start():
    sock.listen()   # Socket lytter etter connections
    print(f"[LISTENING] Server listening on {ADDR} \n") # Melding som viser host adresse som lyttes til
    
    while True: # While løkke som hele tiden accepter og lager en ny thread så lenge det kommer inn en connection
        conn, addr = sock.accept() # Aksepter connection på adressen som kommer inn
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Lager ny thread hvor target er handle funksjonen og den sender conn og addr som argumenter
        thread.start()  # Starter ny thread
        # Printer hvor mange connections som er aktive
        # - 1 fordi listen vil alltid kjøre som en thread før noen har koblet til
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") 

   
# Starter serveren
print("[STARTING] Server is starting")  # Melding om at serveren starter
start() # Kaller på funksjonen til å starte serveren