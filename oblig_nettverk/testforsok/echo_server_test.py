# Test av server, hentet fra https://realpython.com/python-sockets/

import socket

HOST = "127.0.0.1"  # Standard loopback interface adress (localhost)
PORT = 9999 # Port to listen on (non-privileged ports are > 1023)

# socket.socket() creates a socket object that supports the context manager type, so you can use it in a with statement. 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # AF_INET is the Internet address family for IPv4, SOCK_STREAM is the socket type for TCP
    s.bind((HOST,PORT)) # .bind() method is used to associate the socket with a specific network interface and port number
    s.listen()  # listen() enables a server to accept connections. It makes the server a “listening” socket
    conn, addr = s.accept() # .accept() method blocks execution and waits for an incoming connection.

    # After .accept() provides the client socket object conn, an infinite while loop is used to loop over blocking calls to conn.recv(). 
    # This reads whatever data the client sends and echoes it back using conn.sendall().
    # If conn.recv() returns an empty bytes object, b'', that signals that the client closed the connection and the loop is terminated. 
    # The with statement is used with conn to automatically close the socket at the end of the block.
    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)