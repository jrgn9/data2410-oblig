import socket

HOST = '127.0.0.1'
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send(b"GET / HTTP/1.1\r\nHost:HOST\r\n\r\n")
